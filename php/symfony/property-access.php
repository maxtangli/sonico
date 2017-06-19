<?php
use Symfony\Component\PropertyAccess\PropertyAccess;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - provide a united way to access array index, object public variable, getXX/isXX/hasXX, __get.
 *
 * source
 * PropertyAccessor::getValue($objectOrArray, $propertyPath)
 *  $propertyPath = $this->getPropertyPath($propertyPath);
 *  $propertyValues = $this->readPropertiesUntil($zval, $propertyPath, $propertyPath->getLength(), $this->ignoreInvalidIndices);
 *
 * PropertyAccessor::getPropertyPath($propertyPath)
 *  if cache hit: return
 *  return cache.set new PropertyPath($propertyPath) // why cache? regex operations in a long loop may be expensive.
 *
 * PropertyAccessor::readPropertiesUntil(...)
 *  for each path elements
 *   try to call getXX things. for expensive reflections, use cache.
 */

$accessor = PropertyAccess::createPropertyAccessor();

class Person {
    public $firstName;
    private $children = [];

    public function setChildren($children) {
        $this->children = $children;
    }

    public function getChildren() {
        return $this->children;
    }
}

$person = new Person();

$accessor->setValue($person, 'children[0]', new Person);
// equal to $person->getChildren()[0] = new Person()

$accessor->setValue($person, 'children[0].firstName', 'Wouter');
// equal to $person->getChildren()[0]->firstName = 'Wouter'

var_dump('Hello ' . $accessor->getValue($person, 'children[0].firstName')); // 'Wouter'
// equal to $person->getChildren()[0]->firstName