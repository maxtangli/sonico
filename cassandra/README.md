# todo

1. Learning Apache Cassandra.Mat Brown.2015 6h
2. google, summary 1h

# summary

history: inspired by GoogleBigTable amd Amazon Dynamo, developed by Facebook, open source in 2008.

goal: handle big data workloads across multiple nodes without any single point of failure.

design
- data model: each partition key consturcts a list of columns, order by clustering column. secondary index.
- query interface: cql is robust and expressive.
- masterless replication: data rw request -> any node <-> actual node. distributed by partition key, replication factor = 3. tunable consistency. simple scaling by adding nodes.

// https://www.datastax.com/dev/blog/basic-rules-of-cassandra-data-modeling
schema design tips
- goal1: spread data evenly around the cluster: pick partition key carefully.
- goal2: minimize the number of partitions read
- shift from rdb: write is cheap, denormalization and duplication is common.

# example1: scheme

~~~~
CREATE TABLE "users" (
"username" text PRIMARY KEY, // not support auto-incrementing
"email" text, // not support null, default, validation
"encrypted_password" blob
); // may be configured by table properties

INSERT INTO "users"
("username", "email", "encrypted_password")
VALUES (
'alice',
'alice@gmail.com',
0x8914977ed729792e403da53024c6069a9158b8c4
); // no feedback returns.

INSERT INTO "users"
("username", "encrypted_password")
VALUES (
'bob',
0x10920941a69549d33aaee6116ed1f47e19b8e713
); // partial inserts

SELECT "username", "encrypted_password" FROM "users"
WHERE "username" = 'alice';

// update: default create new row
~~~~

# example2: compound primary key

~~~~
// new requirement
// - rows grouped by user
// - rows sorted by creation date
CREATE TABLE "user_status_updates" (
"username" text, // partition key: group rows in same partition.
"id" timeuuid, // clustering column: determine rows-ordering.
"body" text,
PRIMARY KEY ("username", "id") // rows with same primary keys store contiguously
);
CREATE TABLE "users" (
"username" text,
"email" text,
"encrypted_password" blob,
PRIMARY KEY ("username") // each row in its partition, no group
);

INSERT INTO "user_status_updates"
("username", "id", "body")
VALUES (
'alice',
76e7a4d0-e796-11e3-90ce-5f98e903bf02,
'Learning Cassandra!'
);

INSERT INTO "user_status_updates" ("username", "id", "body")
VALUES ('alice', NOW(), 'Alice Update 1'); // NOW() generate timeuuid

SELECT "username", "id", "body", DATEOF("id") // generated time of uuid, not insert time
FROM "user_status_updates";

SELECT * FROM "user_status_updates"
WHERE "username" = 'alice'
AND "id" = 76e7a4d0-e796-11e3-90ce-5f98e903bf02;

// beyond two columns
CREATE TABLE "status_update_replies" (
"status_update_username" text,
"status_update_id" timeuuid,
"id" timeuuid,
"author_username" text,
"body" text,
PRIMARY KEY (
("status_update_username", "status_update_id"), // partition key
"id" // clustering columns
)
);

// Cassandra provide no relation between schemas.
// compound keys represent parent-child relationships: 1:1, 1:n, m:n.
~~~~

# example3: static column

~~~~
CREATE TABLE "users_with_status_updates" (
"username" text,
"id" timeuuid,
"email" text STATIC, // static column has ONLY ONE value per partition key
"encrypted_password" blob STATIC,
"body" text,
PRIMARY KEY ("username", "id")
);

// 1. set email, encrypted_password = xxx where username = alice
// 2. insert into alice partition with body = Learning Cassandra!
INSERT INTO "users_with_status_updates"
("username", "id", "email", "encrypted_password", "body")
VALUES (
'alice',
76e7a4d0-e796-11e3-90ce-5f98e903bf02,
'alice@gmail.com',
0x8914977ed729792e403da53024c6069a9158b8c4,
'Learning Cassandra!'
);

// later inserted rows share static values
INSERT INTO "users_with_status_updates"
("username", "id", "body")
VALUES ('alice', NOW(), 'Another status update');

SELECT * FROM "users_with_status_updates";

// select only static values
SELECT DISTINCT "username", "email", "encrypted_password"
FROM "users_with_status_updates"
WHERE "username" = 'alice';

// 1. static columns will be null
// 2. static-only inserts
INSERT INTO "users_with_status_updates"
("username", "email", "encrypted_password")
VALUES (
'bob',
'bob@gmail.com',
0x10920941a69549d33aaee6116ed1f47e19b8e713
);
INSERT INTO "users_with_status_updates"
("username", "id", "body")
VALUES ('bob', NOW(), 'Bob status update');
~~~~

# example4: select conditions

~~~~
// range slice query for uuid
SELECT "id", DATEOF("id"), "body"
FROM "user_status_updates"
WHERE "username" = 'alice'
AND "id" >= MINTIMEUUID('2014-05-01')
AND "id" <= MAXTIMEUUID('2014-05-31');

// rows paginating in a partition
SELECT "id", DATEOF("id"), "body"
FROM "user_status_updates"
WHERE "username" = 'alice'
LIMIT 3;

// rows couting in a partition
SELECT COUNT(1) FROM "user_status_updates"
WHERE "username" = 'alice';

// rows ordering by cluster in a partition
SELECT "id", DATEOF("id"), "body"
FROM "user_status_updates"
WHERE "username" = 'alice'
ORDER BY "id" DESC;

// reversed cluster ordering in the schema
CREATE TABLE "reversed_user_status_updates" (
"username" text,
"id" timeuuid,
"body" text,
PRIMARY KEY ("username", "id")
) WITH CLUSTERING ORDER BY ("id" DESC);
~~~~

# example5: denormalization vs secondary indexes

~~~~
// denormalization
CREATE TABLE "user_outbound_follows" ( // who do I follow
"follower_username" text,
"followed_username" text,
PRIMARY KEY ("follower_username", "followed_username")
);
CREATE TABLE "user_inbound_follows" ( // who followed me
"followed_username" text,
"follower_username" text,
PRIMARY KEY ("followed_username", "follower_username")
);

// secondary indexes: one column only, equality only, slower than primary key.
CREATE TABLE "user_follows" (
"followed_username" text,
"follower_username" text,
PRIMARY KEY ("followed_username", "follower_username")
);
CREATE INDEX ON "user_follows" ("follower_username"); // suited for low-cardinality columns, why?
~~~~

# example6: performance issues

~~~~
// not recommended, where in may retrieve multiple partitions
// If I follow F users and want a page of size P for my home timeline
// - query F partitions for P rows each
// - perform an ordered merge of FxP rows in order to retrieve only the most recent P
SELECT "username", "id", UNIXTIMESTAMPOF("id"), "body"
FROM "user_status_updates"
WHERE "username" IN ('carol', 'dave') 
ORDER BY "id" DESC
LIMIT 2;

// partial denormalization
// - write row to all followers
// - query F partitions for P rows total
// - sort P rows
CREATE TABLE "home_status_update_ids" (
"timeline_username" text,
"status_update_id" timeuuid,
"status_update_username" text,
PRIMARY KEY ("timeline_username", "status_update_id")
)WITH CLUSTERING ORDER BY ("status_update_id" DESC);

BEGIN BATCH
INSERT INTO "user_status_updates"
("username", "id", "body")
VALUES(
'carol', 65cd8320-2ad7-11e4-8069-5f98e903bf02,
'carol update 3');
INSERT INTO "home_status_update_ids" // when post, insert keys into all followers' homeline
("timeline_username", "status_update_id",
"status_update_username")
VALUES
('alice', 65cd8320-2ad7-11e4-8069-5f98e903bf02, 'carol');
APPLY BATCH;

SELECT "status_update_username", "status_update_id"
FROM "home_status_update_ids"
WHERE "timeline_username" = 'alice';
SELECT * FROM "user_status_updates" // when select, use keys
WHERE "username" IN ('dave', 'carol')
AND "id" IN (
a05b90b0-2ada-11e4-8069-5f98e903bf02,
65cd8320-2ad7-11e4-8069-5f98e903bf02
);

// fully denormalization
// - write row to all followers
// - query a partiton
CREATE TABLE "home_status_updates" (
"timeline_username" text,
"status_update_id" timeuuid,
"status_update_username" text,
"body" text,
PRIMARY KEY ("timeline_username", "status_update_id")
) WITH CLUSTERING ORDER BY ("status_update_id" DESC);

BEGIN BATCH
INSERT INTO "user_status_updates"
("username", "id", "body")
VALUES
('carol',
cacc7de0-2af9-11e4-8069-5f98e903bf02,
'carol update 4'
);
INSERT INTO "home_status_updates"
("timeline_username", "status_update_id", "status_update_username",
"body")
VALUES (
'alice',
cacc7de0-2af9-11e4-8069-5f98e903bf02,
'carol',
'carol update 4'
);
APPLY BATCH;

SELECT "status_update_username", "status_update_id", "body"
FROM "home_status_updates"
WHERE "timeline_username" = 'alice';
~~~~

# example7: lightweight transaction

~~~~
// insert: default override. 
// - use UUID or globally unique nature key to avoid.
// - use IF NOT EXISTS to avoid.
INSERT INTO "users"
("username", "email", "encrypted_password")
VALUES
('happycorp', 'media@happycorp.com',
0x368200fa910c16cc644f3512e63b541c85fa2a3c)
IF NOT EXISTS; 

// update: default may insert. use optimistic locking with conditional updates to avoid.
UPDATE "users"
SET "location" = 'New York, NY', "version" = NOW()
WHERE "username" = 'happycorp'
IF "version" = ec0c1fb7-321f-11e4-8eeb-5f98e903bf02; 
~~~~

# example8: collection

~~~~
// SET
ALTER TABLE "user_status_updates"
ADD "starred_by_users" SET<text>;

UPDATE "user_status_updates"
SET "starred_by_users" = {'bob'}
WHERE "username" = 'alice'
AND "id" = 76e7a4d0-e796-11e3-90ce-5f98e903bf02;

UPDATE "user_status_updates"
SET "starred_by_users" = "starred_by_users" + {'carol'}
WHERE "username" = 'alice'
AND "id" = 76e7a4d0-e796-11e3-90ce-5f98e903bf02;

UPDATE "user_status_updates
SET "starred_by_users" = "starred_by_users" - {'dave'}
WHERE "username" = 'alice'
AND "id" = 76e7a4d0-e796-11e3-90ce-5f98e903bf02;

// LIST
ALTER TABLE "user_status_updates"
ADD "shared_by" LIST<text>;

UPDATE "user_status_updates"
SET "shared_by" = ['bob']
WHERE "username" = 'alice'
AND "id" = 76e7a4d0-e796-11e3-90ce-5f98e903bf02;

UPDATE "user_status_updates"
SET "shared_by"[1] = 'robert'
WHERE "username" = 'alice'
AND "id" = 76e7a4d0-e796-11e3-90ce-5f98e903bf02;

// MAP
ALTER TABLE "users"
ADD social_identities MAP<text,bigint>;

UPDATE "users"
SET "social_identities" = {'twitter': 353637}
WHERE "username" = 'alice';

UPDATE "users"
SET "social_identities"['instagram'] = 9839025,
"social_identities"['yo'] = 25
WHERE "username" = 'alice';

DELETE "social_identities"['instagram']
FROM "users"
WHERE "username" = 'alice';

// secondary index on collection
CREATE INDEX ON "user_status_updates" ("starred_by_users");

SELECT * FROM "user_status_updates"
WHERE "starred_by_users" CONTAINS 'alice';

// collection limits
// - no partial collection select support
// - 64KB size limit, truncated if overflow
// - cannot select collection in WHERE..IN
// - perfomance issue: write-with-reading for e.g. [i]=v, -[i]

// TUPLE
ALTER TABLE "users"
ADD "education" frozen <tuple<text, int>>;

UPDATE "users"
SET "education" = ('Big Data University', 2003)
WHERE "username" = 'alice';

UPDATE "users"
SET "education" = ('BDU') // at least first value required
WHERE "username" = 'alice';

CREATE INDEX ON "users" ("education");

// user-defined type
CREATE TYPE "education_information" (
"school_name" text,
"graduation_year" int
);

ALTER TABLE "users"
ADD "education" frozen <"education_information">;

UPDATE "users"
SET "education" = {
"school_name": 'Big Data University',
"graduation_year": 2003
}WHERE "username" = 'alice';

CREATE INDEX ON "users" ("education");

SELECT "username", "education"."school_name"
FROM "users"
WHERE "username" = 'alice';
~~~~

# example9: time-series
# example10: data distribution

~~~~
goals
- data distribution: transparent, by partition key token into virtual nodes(optimize rebalancing), which owned by physical nodes.
- fault tolerance: masterless replication with replication factor=3, by storing virual nodes in multiple physical nodes randomly.
- consistency: tunable consistency by consistency levels, e.g. ONE,ALL,QUORUM
- conflict resolution: timestamp, last-write-wins.
- deleting data: tombstone.

CREATE KEYSPACE "my_status"
WITH REPLICATION = {
'class': 'SimpleStrategy',
'replication_factor': 3
};
~~~~

# impl

~~~~
USE my_status;
LIST users; // print info grouped by RowKey
GET users['happycorp']['email'] AS ascii;

RowKey: happycorp
=> (name=,value=,timestamp=) // column1
=> (name=,value=,timestamp=) // column2 
=> (name=hash(starred_by_users:dave),value=,timestamp=) // set and map collection column stored as multiple columns
=> (name=hash(shared_by:uuid)) // list collection columns stored as multiple columns
... // empty column is not storaged

// each rows are stored non-contiguously

RowKey: study
...

// cluster keys: columns list's order? 
// secondary indexes: similar to rdb indexes?
~~~~
