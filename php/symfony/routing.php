<?php

use Symfony\Component\Routing\Matcher\UrlMatcher;
use Symfony\Component\Routing\RequestContext;
use Symfony\Component\Routing\Route;
use Symfony\Component\Routing\RouteCollection;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - maps an HTTP request to a set of configuration variables
 *
 * design
 * - Route: a mapping.
 * - RouteCollection: a collection of route, support overall modification.
 *
 * - RequestContext: wrap request arguments.
 * - RequestContextAwareInterface <- UrlMatcherInterface <- UrlMatcher
 * - RequestMatcherInterface <- UrlMatcher($routes, $context)
 * - TraceableUrlMatcher extends UrlMatcher
 * - RedirectableUrlMatcherInterface <- RedirectableUrlMatcher extends UrlMatcher
 *
 * code
 * $matcher->match('/foo');
 *  foreach $route
 *   $route->compile(): match regex, hostRegex, http method
 */

$route = new Route('/foo', ['_controller' => 'MyController']);
$routes = new RouteCollection();
$routes->add('route_name', $route);

$context = new RequestContext('/');

$matcher = new UrlMatcher($routes, $context);

$parameters = $matcher->match('/foo');
// array('_controller' => 'MyController', '_route' => 'route_name')

$route = new Route(
    '/archive/{month}', // path
    array('_controller' => 'showArchive'), // default values
    array('month' => '[0-9]{4}-[0-9]{2}', 'subdomain' => 'www|m'), // requirements
    array(), // options
    '{subdomain}.example.com', // host
    array('http', 'https'), // schemes
    array('get', 'post') // methods
);

// ...

$parameters = $matcher->match('/archive/2012-01');
// array(
//     '_controller' => 'showArchive',
//     'month' => '2012-01',
//     'subdomain' => 'www',
//     '_route' => ...
//  )

$parameters = $matcher->match('/archive/foo');
// throws ResourceNotFoundException