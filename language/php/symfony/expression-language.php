<?php
use Symfony\Component\ExpressionLanguage\ExpressionLanguage;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - allow users to use expressions inside configuration for more complex logic,
 * - e.g. route matching rules, validation rules.
 *
 * design
 * - Token: type + value + cursor.
 * - Lexer: tokenize($expression) by regex -> Token[] -> TokenStream for convenient parse.
 * - Node <- ConcreteNode: node.compile(), node.evaluate().
 * - Parser: parse($tokenStream) by recursively build a AST -> ParsedExpression=root Node.
 * - Compiler: compile($node) -> node.compile() -> php source string.
 * - Cache: cache ParsedExpression.
 */

$language = new ExpressionLanguage();

// execute
var_dump($language->evaluate('1 + 2')); // displays 3
var_dump($language->compile('1 + 2')); // displays (1 + 2)

// dumping AST
$ast = $language
    ->parse('1 + 2', [])
    ->getNodes();
echo $ast->dump(), "\n";
var_dump($ast->toArray());