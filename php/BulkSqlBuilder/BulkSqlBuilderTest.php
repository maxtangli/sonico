<?php

require_once "BulkSqlBuilder.php";

class BulkSqlBuilderTest extends PHPUnit\Framework\TestCase {
    function testBuilder() {
        $builder = new BulkSqlBuilder('replace into XXTable(FieldA, FieldB, FieldC) values', 2);
        $this->assertEmpty($builder->build());

        $builder->addValue('(A1,B1,C1)');
        $this->assertEquals(['replace into XXTable(FieldA, FieldB, FieldC) values(A1,B1,C1);'], $builder->build());

        $builder->addValue('(A2,B2,C2)');
        $this->assertEquals(['replace into XXTable(FieldA, FieldB, FieldC) values(A1,B1,C1),(A2,B2,C2);'], $builder->build());

        $builder->addValue('(A3,B3,C3)');
        $this->assertEquals(['replace into XXTable(FieldA, FieldB, FieldC) values(A1,B1,C1),(A2,B2,C2);', 'replace into XXTable(FieldA, FieldB, FieldC) values(A3,B3,C3);'], $builder->build());
    }
}
