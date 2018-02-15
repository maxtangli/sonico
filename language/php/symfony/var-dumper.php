<?php
require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - per types specialized view
 * - support dump internal reference
 * - output formats: cli, html
 * - output buffer context
 *
 * design
 * - Cloner: create an intermediate representation of any PHP variable, which is class Data.
 * - Dumper: output a simple string representation of a Data input.
 * - Caster: cast a variable's inner properties into array, thus support custom view.
 */

/**
 * VarDumper::dump($var);
 *  $cloner = new VarCloner();
 *  $dumper = 'cli' === PHP_SAPI ? new CliDumper() : new HtmlDumper();
 *  $dumper->dump($cloner->cloneVar($var));
 *
 * AbstractCloner::cloneVar($var)
 *  set_error_handler // to cast errors into exception?
 *  try $data = $this->doClone($var); catch $e: throw
 *  restore_error_handler()
 *  return new Data($data);
 *
 * VarCloner::doClone($var)
 *  $queue = array(array($var));
 *  ...
 *  $zval = symfony_zval_info($k, $refs);
 *  switch ($zval['type'])
 *   $stub = ...
 *  ...
 *  return $queue
 *
 * Data::__construct(array $data)
 *
 * Dumper: dump(Data $data). AbstractDumper -> CliDumper -> HtmlDumper.
 * AbstractDumper::dump(Data $data, $output = null)
 *  handle $output
 *  try $data->dump($this); $this->dumpLine(-1);
 *
 * Data::dump(DumperInterface $dumper)
 * Data::dumpItem($dumper, $cursor, &$refs, $item)
 *  switch $item->type
 *   $dumper->dumpXXType($item)
 *
 * CliDumper::dumpString(...)
 *
 * HtmlDumper
 *  // wrap CliDumper into html output format
 */

$var = array(
    'a simple string' => "in an array of 5 elements",
    'a float' => 1.0,
    'an integer' => 1,
    'a boolean' => true,
    'an empty array' => array(),
);
dump($var);
/**
array:5 [
  "a simple string" => "in an array of 5 elements"
  "a float" => 1.0
  "an integer" => 1
  "a boolean" => true
  "an empty array" => []
]
 */

class ReferenceExample
{
    public $info = "Circular and sibling references are displayed as `#number`.\nHovering them highlights all instances in the same dump.\n";
}
$var = new ReferenceExample();
$var->aCircularReference = $var;
dump($var);
/**
ReferenceExample {#5
  +info: """
    Circular and sibling references are displayed as `#number`.\n
    Hovering them highlights all instances in the same dump.\n
    """
  +"aCircularReference": ReferenceExample {#5}
}
 */