<?php

use Symfony\Component\Finder\Finder;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - provide a flexible file search api.
 *
 * design
 * - beautiful iterators chain!
 *
 * code
 * - criteria: set field.
 * - getIterator: parse criteria into iterators chain.
 */

$finder = new Finder();
$finder->in(__DIR__)->name('*.php')->sortByName()->depth(0);
echo implode("\n", iterator_to_array($finder));