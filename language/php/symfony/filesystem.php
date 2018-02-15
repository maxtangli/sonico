<?php

use Symfony\Component\Filesystem\Filesystem;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - provide exception style filesystem api.
 *
 * code
 * - wrap php file functions by adding exception.
 */

$fs = new Filesystem();
$file = 'tmp.txt';
$fs->touch($file);
$fs->remove($file);
var_dump($fs->exists($file));