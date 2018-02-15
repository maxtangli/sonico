<?php

use Symfony\Component\Security\Csrf\CsrfTokenManager;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - manage csrf token.
 *
 * design
 * - TokenGenerator <- UriSafeToken: base64_encode(random_bytes(len))
 * - TokenStorage <- Session
 * - TokenManager = Generator + Storage
 * - Token = id + value
 */

$csrfTokenManager = new CsrfTokenManager();

$tokenId = 'sonico';
echo $csrfTokenManager->getToken($tokenId), "\n";
echo $csrfTokenManager->getToken($tokenId), "\n";
echo $token = $csrfTokenManager->refreshToken($tokenId), "\n";
echo $csrfTokenManager->isTokenValid($token) ? 'valid' : 'invalid', "\n";
$csrfTokenManager->removeToken($tokenId);
echo $csrfTokenManager->isTokenValid($token) ? 'valid' : 'invalid', "\n";