<?php
require_once __DIR__ . '/vendor/autoload.php';

use Symfony\Component\Asset\Package;
use Symfony\Component\Asset\Packages;
use Symfony\Component\Asset\PathPackage;
use Symfony\Component\Asset\UrlPackage;
use Symfony\Component\Asset\VersionStrategy\StaticVersionStrategy;

/**
 * goal
 * - abstraction of resource url
 *
 * design
 *  path    -> Package: getVersion($path), getUrl($path)
 *  version -> Strategy: getVersion($path), applyVersion($path)
 */

$versionStrategy = new StaticVersionStrategy('v1', '%s?v=%s');
$defaultPackage = new Package($versionStrategy);
$namedPackages = [
    'img' => new UrlPackage('http://img.example.com/', $versionStrategy),
    'doc' => new PathPackage('/somewhere/deep/for/documents', $versionStrategy),
];
$packages = new Packages($defaultPackage, $namedPackages);

echo $packages->getUrl('/main.css') . PHP_EOL;
// result: /main.css?v1

echo $packages->getUrl('/logo.png', 'img') . PHP_EOL;
// result: http://img.example.com/logo.png?v1

echo $packages->getUrl('/resume.pdf', 'doc') . PHP_EOL;
// result: /somewhere/deep/for/documents/resume.pdf?v1
