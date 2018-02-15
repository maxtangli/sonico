<?php

use Symfony\Component\EventDispatcher\Event;
use Symfony\Component\EventDispatcher\EventDispatcher;

require_once __DIR__ . '/vendor/autoload.php';

/**
 * goal
 * - a event&listener system framework.
 *
 * design
 * - Event: $propagationStopped.
 * - Listener: free custom classes.
 * - EventDispatcherInterface: add/remove/sort listeners, dispatch event.
 *
 * more features
 * - GenericEvent: simple event by name and array arguments.
 * - ImmutableEventDispatcher(EventDispatcherInterface)
 * - ContainerAwareEventDispatcher(DependencyInjection\ContainerInterface)
 * - TraceableEventDispatcher($dispatcher, $stopwatch, $logger)
 */
class PokemonAppearedEvent extends Event {
    const NAME = 'pokemon.appeared';
    private $pokemon;

    function __construct($pokemon) {
        $this->pokemon = $pokemon;
    }

    function getNo() {
        $a = [25 => 'pikachu'];
        $v = array_search($this->getPokemon(), $a);
        return $v ?: '?';
    }

    function getPokemon() {
        return $this->pokemon;
    }
}

class TrainerListener {
    private $trainer;

    function __construct($trainer) {
        $this->trainer = $trainer;
    }

    function getTrainer() {
        return $this->trainer;
    }

    function say($message) {
        echo $message . "\n";
    }

    function onPokemonAppeared(Event $event) {
        if ($event instanceof PokemonAppearedEvent) {
            $message = sprintf("pokemon no.%s %s, get daze!", $event->getNo(), $event->getPokemon());
            $this->say($message);
            $event->stopPropagation();
        }
    }

    function onGameover() {
        $message = 'money = money / 2.';
        $this->say($message);
    }
}

$dispatcher = new EventDispatcher();

$trainerListener = new TrainerListener('satoshi');
$dispatcher->addListener(PokemonAppearedEvent::NAME, [$trainerListener, 'onPokemonAppeared']);
$dispatcher->addListener('gameover', [$trainerListener, 'onGameover']);

$event = new PokemonAppearedEvent('pikachu');
$dispatcher->dispatch(PokemonAppearedEvent::NAME, $event);
$dispatcher->dispatch('gameover');