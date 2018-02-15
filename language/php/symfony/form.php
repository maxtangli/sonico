<?php

use Symfony\Component\Form\Extension\Core\Type\DateType;
use Symfony\Component\Form\Extension\Core\Type\FormType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\Extension\HttpFoundation\HttpFoundationExtension;
use Symfony\Component\Form\Forms;
use Symfony\Component\HttpFoundation\Request;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - a form system support: request, csrf, templating, translation, validation.
 *
 * design
 * - FormFactoryBuilderInterface: addExtension, getFormFactory
 * - FormFactoryInterface: createBuilder
 * - FormBuilderInterface: add($child), getForm
 * - FormInterface: handleRequest
 * - FormConfigBuilderInterface: getRequestHandler
 * - FormConfigInterface: getRequestHandler
 *
 * code
 * Form: __construct(FormConfigInterface $config)
 * Form: handleRequest($request)
 *  $this->config->getRequestHandler()->handleRequest($this, $request);
 *   HttpFoundationRequestHandler
 *    check method
 *    extract data
 *    $form->submit($data, 'PATCH' !== $method);
 */

$formFactory = Forms::createFormFactoryBuilder()
    ->addExtension(new HttpFoundationExtension())
    ->getFormFactory();

$formBuilder = $formFactory->createBuilder(FormType::class, null, [
    'method' => 'GET'
]);

$form = $formFactory->createBuilder()
    ->add('task', TextType::class)
    ->add('dueDate', DateType::class)
    ->setMethod('GET')
    ->getForm();

$_GET['task'] = 'learn symfony';
$_GET['dueDate'] = '2017-07-18';
$request = Request::createFromGlobals();
// form name set by template?

// bad design? should throw Exception for invalid request rather than return null.
$form->handleRequest($request);

if ($form->isSubmitted() && $form->isValid()) {
    $data = $form->getData();

    var_dump($data);
    // ... perform some action, such as saving the data to the database

//    $response = new RedirectResponse('/task/success');
//    $response->prepare($request);
//
//    return $response->send();
} else {
    echo "error";
}

// ...