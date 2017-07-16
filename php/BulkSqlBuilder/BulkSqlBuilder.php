<?php

class BulkSqlBuilder {
    private $baseSql;
    private $valueCountLimit;
    private $result;
    private $lastSqlSize;

    /**
     * @param string $baseSql e.g. "replace into XXTable(FieldA, FieldB, ...) values "
     * @param int $valueCountLimit
     */
    function __construct(string $baseSql, int $valueCountLimit = 5000) {
        $this->baseSql = $baseSql;
        $this->valueCountLimit = $valueCountLimit;

        $this->result = [];
        $this->lastSqlSize = 0;
    }

    /**
     * @param string $value e.g. "(A, B, ...)"
     * @return $this
     */
    function addValue(string $value) {
        if (empty($this->result) || $this->lastSqlSize >= $this->valueCountLimit) {
            $sql = $this->baseSql . "{$value};";
            $this->lastSqlSize = 0;
        } else {
            $lastSql = array_pop($this->result);
            $sql = substr($lastSql, 0, -1) . ",{$value};";
        }
        $this->result[] = $sql;
        $this->lastSqlSize = $this->lastSqlSize + 1;
        return $this;
    }

    /**
     * @return string[]
     */
    function build() {
        return $this->result;
    }
}