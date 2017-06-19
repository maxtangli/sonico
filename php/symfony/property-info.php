<?php

use Symfony\Component\PropertyInfo\Extractor\PhpDocExtractor;
use Symfony\Component\PropertyInfo\Extractor\ReflectionExtractor;
use Symfony\Component\PropertyInfo\PropertyInfoExtractor;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - provide a obvious way to examine type information.
 *
 * design
 * - PropertyInfoExtractor: mediator of extractors.
 * - Extractor: implementation of extract behaviour.
 */

$reflectionExtractor = new ReflectionExtractor();
$phpDocExtractor = new PhpDocExtractor();

$listExtractors = [$reflectionExtractor];
$typeExtractors = [$reflectionExtractor];
$descriptionExtractors = [$phpDocExtractor];
$accessExtractors = [$reflectionExtractor];
$propertyInfoExtractor = new PropertyInfoExtractor($listExtractors, $typeExtractors, $descriptionExtractors, $accessExtractors);

class Yome {
    public $yome = 'nanoha';
    public $darling = 'sonico';
    public $pet = 'reisen';
    private $previous = 'saki';

    function getDearListNoReturnType() {
        return [$this->yome, $this->darling];
    }

    /**
     * A list of dears.
     * wahaha.
     * wahahaha.
     * wahahahaha.
     * @return array
     */
    function getDearList(): array {
        return [$this->yome, $this->darling];
    }
}

$properties = $propertyInfoExtractor->getProperties(Yome::class);
$types = $propertyInfoExtractor->getTypes(Yome::class, 'dearList');
$noTypes = $propertyInfoExtractor->getTypes(Yome::class, 'dearListNoReturnType');
$descriptions = $propertyInfoExtractor->getShortDescription(Yome::class, 'dearList');
$longDescriptions = $propertyInfoExtractor->getLongDescription(Yome::class, 'dearList');
$isReadable = $propertyInfoExtractor->isReadable(Yome::class, 'dearList');
$isWritable = $propertyInfoExtractor->isWritable(Yome::class, 'dearList');
var_dump($properties, $types, $noTypes, $descriptions, $longDescriptions, $isReadable, $isWritable);