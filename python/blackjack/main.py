import collections
import random

if __name__ == '__main__':
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    deck = [Card(rank, suit) for suit in suits for rank in ranks]

    hand = []

    random.shuffle(deck)
    hand.append(deck.pop())
    hand.append(deck.pop())

    print(hand)
    handAllowDraw = True and len(deck) > 0  # todo
    while handAllowDraw and input('draw (y/n)?') == 'y':
        hand.append(deck.pop())
        print(hand)

    print('over')

"""
goal:
    a blackjack cmd game = a practice to master python basics
flow:
    shuffle deck
    hand = deck.pop 2
    while hand.allowDraw and user.draw:
        hand <- deck.pop 1
todo:
    - [x] hello blackjack 0.5h
    - [ ] impl handAllowDraw
"""