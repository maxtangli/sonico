<?php
use Symfony\Component\Serializer\Encoder\JsonEncoder;
use Symfony\Component\Serializer\Encoder\XmlEncoder;
use Symfony\Component\Serializer\Normalizer\ObjectNormalizer;
use Symfony\Component\Serializer\Serializer;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - object <-> array <-> json,xml,yaml,csv
 *
 * design
 * - Serializer: mediator of encoders and normalizers
 * - Normalizer,Denormalizer: object <-> array
 * - Encoder,Decoder: array <-> json,xml,yaml,csv
 *
 * source
 * serialize
 *  if encoder->needsNormalization: // NormalizationAwareInterface
 *    data = normalize data // call proper normalizer
 *  return encode data // call proper encoder
 */

$encoders = [new XmlEncoder(), new JsonEncoder()];
$normalizers = [new ObjectNormalizer()];
$serializer = new Serializer($normalizers, $encoders);

class Person
{
    private $age;
    private $name;
    private $sportsman;

    // Getters
    public function getName()
    {
        return $this->name;
    }

    public function getAge()
    {
        return $this->age;
    }

    // Issers
    public function isSportsman()
    {
        return $this->sportsman;
    }

    // Setters
    public function setName($name)
    {
        $this->name = $name;
    }

    public function setAge($age)
    {
        $this->age = $age;
    }

    public function setSportsman($sportsman)
    {
        $this->sportsman = $sportsman;
    }
}

$person = new Person();
$person->setName('foo');
$person->setAge(99);
$person->setSportsman(false);
$jsonContent = $serializer->serialize($person, 'json');
// $jsonContent contains {"name":"foo","age":99,"sportsman":false}
echo $jsonContent; // or return it in a Response

$data = <<<EOF
<person>
    <name>foo</name>
    <age>99</age>
    <sportsman>false</sportsman>
</person>
EOF;
$person = $serializer->deserialize($data, Person::class, 'xml');
var_dump($person);