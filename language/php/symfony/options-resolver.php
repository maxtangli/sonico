<?php

use Symfony\Component\OptionsResolver\OptionsResolver;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - a options resolver support: required exist/type/value, default, normalizer.
 *
 * code
 * - very straight implementation.
 */

$resolver = new OptionsResolver();
$resolver->setDefaults([
    'host' => 'smtp.example.org',
    'username' => 'user',
    'password' => 'pa$$word',
    'port' => 25,
    'encryption' => null,
]);
$options = $resolver->resolve([
    'username' => 'reisen',
    'password' => 'touhou07'
]);
var_dump($options);