<?php

use Symfony\Component\Console\Application;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Question\Question;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - console application with command support and other rich features.
 *
 * design
 * - Application
 * - Command
 * - Terminal: handle terminal style by proc_open('stty ...')
 * - InputInterface <- Input <- ArgvInput, ArrayInput, StringInput extends ArgvInput
 * - InputDefinition: a set of InputArgument and InputOption
 * - OutputInterface <- StreamOutput <- ConsoleOutput, BufferedOutput, NullOutput
 *
 * code
 * Application.new
 *  add default commands: name, alias -> command
 * Application.addCommand
 * Application.run
 *  set terminal style
 *  init input&output stream, add style
 *  try run
 *  catch exception: pirnt it
 *
 * Command.new
 *  configure()
 * Command.run
 *  initialize()
 *  if interactive() : interact()
 *  $input->validate();
 *  execute()
 *
 * HelperCommand
 * ListCommand
 */
class HelloCommand extends Command {
    protected function configure() {
        $this->setName('hello')
            ->setDescription('say hello')
            ->setHelp('say hello to user.')
            ->addArgument('target', InputArgument::OPTIONAL, 'target to say to', 'symfony');
    }

    protected function execute(InputInterface $input, OutputInterface $output) {
        $target = $input->getArgument('target');
        $output->writeln("hello, {$target}!");

        /** @var QuestionHelper $helper */
        $helper = $this->getHelper('question');
        $question = new Question('yome?', 'nanoha');
        $yome = $helper->ask($input, $output, $question);
        $output->writeln("hello, {$yome}!");
    }
}

$application = new Application('hello', '0.1');
$commands = [new HelloCommand()];
$application->addCommands($commands);
$application->run();