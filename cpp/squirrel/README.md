# installation

~~~~
wget your_url
tar -xvzf your_file 
cd squirrel3
make sq64
~~~~

/bin/sq: an interactive interpreter.
/lib: libsqstdlib.a, libsquirrel.a

# language

http://www.squirrel-lang.org/squirreldoc/reference/index.html

execution context
- function root(root table): ::foo.
- function environment object(this): this.foo.
- function stack frame: local variables.
- scope determination: local -> environment -> root.

keywords
- type: null true false enum, class constructor static extends, function return yield, const, :: this local.
- operation: typeof instanceof, clone, in delete.
- control: if else swtich case default, while for foreach continue break, throw try catch.
- ?: base

data types
- dynamically typed language
- Enumerations and Contants are a compile-time feature
- basic types:  integer, float, string, null, table, array, function, generator, class, instance, bool, thread and userdata.

~~~~
// table: associative container. support json syntax.
local t={a=10,b="ten"}

t.c <- "shi", t[c] <- "shi" // slot creation. error way since t.c not existed: t.c = "shi"

delete t.c

// array: dynamic sized sequence.
local a=['a','b','c']

// function: support local, default params, variable-length params, lambda.
local function ciao(a,b,c) { return a + b - c; }
local ciao = function(a, b, c) { return a + b - c; }
local ciao = @(a,b,c) a + b - c

function ciao(a,b,c) { return a + b - c; }
this.ciao <- function(a, b, c) { return a + b - c; }

T <- {}
function T::ciao(a,b,c) { return a + b - c; }
T.ciao <- function(a, b, c) { return a + b - c; }

// generator: function that supports yield.

// class: associative container. created through 'class expression', can change before the first class instance created. inheritance happens when created. support attributes as metadata, metamethods e.g. _add, _get etc..

class Foo {
    constructor(a) {testy = ["stuff",1,2,3,a];}
    function PrintTesty() {...}
    testy = null;
}
Foo <- class {...}

FakeNamespace <- { Utils = {} }

Foo.stuff <- 10;

// class instance: associative container. can't change key, can change value.

local foo = Foo(); // a verbatim copy of Foo, so always use constructor.

// user data: blob

// thread

// weak reference
~~~~

# embedding

memory management
- RC + GC: default.
- RC only: to save space.

vm init
~~~~
HSQUIRRELVM v;
v = sq_open(1024); // 1024 size stack
...
sq_close(v);
~~~~

vm config
~~~~
SQUIRREL_API void sq_seterrorhandler(HSQUIRRELVM v);

SQUIRREL_API void sq_setdebughook(HSQUIRRELVM v);

SQRESULT sq_compile(HSQUIRRELVM v,SQREADFUNC read,SQUserPointer p,
            const SQChar *sourcename,SQBool raiseerror);
~~~~

calling function by exchange values by stack
~~~~
// foo(1,2.0,"three");
sq_pushroottable(v);
sq_pushstring(v,"foo",-1);
sq_get(v,-2); //get the function from the root table
sq_pushroottable(v); //'this' (function environment object)
sq_pushinteger(v,1);
sq_pushfloat(v,2.0);
sq_pushstring(v,"three",-1);
sq_call(v,4,SQFalse);
sq_pop(v,2); //pops the roottable and the function
~~~~

pass c data
~~~~
// pass function

// pass array
sq_arrayxxx()

// pass userdata
~~~~
