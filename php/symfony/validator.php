<?php
use Symfony\Component\Validator\Constraints\Length;
use Symfony\Component\Validator\Constraints\NotBlank;
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints as Assert;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - validate values following JSR-303 Bean Validation specification.
 *
 * design
 * - ValidatorInterface: return a ContextualValidatorInterface for a validation.
 * - ContextualValidatorInterface: generated for each validate action.
 * - abstract Constraint <- error code&message
 * - abstract ConstraintValidator <- if error, build violation
 * - ConstraintViolation: hold values.
 *
 */

$validator = Validation::createValidator();

// validate value
$violations = $validator->validate('saber', [
    new Length(['min' => 10]),
    new NotBlank(),
]);

if (0 !== count($violations)) {
    // there are errors, now you can show them
    foreach ($violations as $violation) {
        echo $violation->getMessage() . "\n";
    }
}

// validate object
$validator = Validation::createValidatorBuilder()
    ->enableAnnotationMapping()
    ->getValidator();

class Author {
    /**
     * @Assert\NotBlank()
     * @Assert\Length(min=3)
     */
    private $firstName;
    private $password;

    function getFirstName() {
        return $this->firstName;
    }

    function setFirstName($firstName) {
        $this->firstName = $firstName;
    }
}

$author = new Author();
$author->setFirstName('sonico');
$errors = $validator->validate($author);
if (count($errors) > 0) {
    echo (string)$errors, "\n";
} else {
    echo "passed.", "\n";
}