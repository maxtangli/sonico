<?php

use Symfony\Component\Cache\Adapter\ArrayAdapter;
use Symfony\Component\Cache\Simple\ArrayCache;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - implement PSR-6 cache, PSR-16 simple cache
 *
 * design
 * - ArrayTrait <- ArrayAdaptor implements AdapterInterface, ArrayCache implements CacheInterface
 * - CacheItem implements CacheItemInterface // also used as util class
 * - tests // base test classes to test common interface
 * - ChainCache // seems not practical to chain caches together?
 * - TraceableCache // wrap a cache by adding statistics
 */

$cache = new ArrayCache();
$cache->set('yome', 'sonico');
//... as time past
if ($cache->has('yome')) { // if hit
    echo $cache->get('yome');
}
$cache->clear();

$cache = new ArrayAdapter();
$yome = $cache->getItem('yome');
$yome->set('sonico');
$cache->save($yome);
//... as time past
$yome = $cache->getItem('yome');
if ($yome->isHit()) {
    echo $yome->get();
}