<?php
use Symfony\Component\Debug\Debug;

require_once __DIR__ . '/vendor/autoload.php';

explode('', null);
/**
PHP Warning:  explode(): Empty delimiter in D:\SE\sonico\php\symfony\debug.php on line 7
 */

Debug::enable();
explode('', null);
/**
PHP Fatal error:  Uncaught Symfony\Component\Debug\Exception\ContextErrorException: Warning: explode(): Empty delimiter in D:\SE\sonico\php\symfony\debug.php:13
Stack trace:
#0 {main}
thrown in D:\SE\sonico\php\symfony\debug.php on line 13
 */