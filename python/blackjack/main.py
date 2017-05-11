import collections
import random
import unittest


class Card:
    def __init__(self, rank, suit='spades'):
        # todo validate
        self.rank = rank
        self.suit = suit

    def is_number(self):
        return not self.is_ace()

    def is_ace(self):
        return self.rank in list('JQK')

    def get_point(self):
        return self.rank if self.is_number() else 11

    def get_min_point(self):
        return self.rank if self.is_number() else 1


class Hand(list):
    def get_points(self):
        max_points = sum(map(Card.get_point, self))
        min_points = sum(map(Card.get_min_point, self))
        points = max_points
        while points > min_points:
            if points <= 21:
                return points
            else:
                points -= 10
        return points

    def is_bust(self):
        return self.get_points() > 21

    def allow_draw(self):
        return not self.is_bust() and len(self) <= 5


class TestBlackjack(unittest.TestCase):
    def test_card(self):
        self.assertEqual(2, Card(2).get_point())
        self.assertEqual(11, Card('J').get_point())

    def test_hand(self):
        self.assertEqual(2, Hand([Card(2)]).get_points())
        self.assertEqual(11, Hand([Card('J')]).get_points())
        self.assertEqual(13, Hand([Card(2), Card('J')]).get_points())
        self.assertEqual(14, Hand([Card(2), Card('J'), Card('J')]).get_points())
        self.assertEqual(15, Hand([Card(2), Card('J'), Card('J'), Card('J')]).get_points())
        self.assertEqual(15, Hand([Card(2), Card('J'), Card('J'), Card('J'), Card(10)]).get_points())
        self.assertEqual(24, Hand([Card(2), Card('J'), Card('J'), Card(10), Card(10)]).get_points())


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     # Card = collections.namedtuple('Card', ['rank', 'suit'])
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#     deck = [Card(rank, suit) for suit in suits for rank in ranks]
#
#     hand = []
#
#     random.shuffle(deck)
#     hand.append(deck.pop())
#     hand.append(deck.pop())
#
#     print(hand)
#     handAllowDraw = True # todo
#     while handAllowDraw and len(deck) > 0 and input('draw (y/n)?') == 'y':
#         hand.append(deck.pop())
#         print(hand)
#
#     print('over')

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

    - [x] Hand.get_points() 1h
    - [x] impl handAllowDraw 0.1h
    
    - [ ] adapt main
"""
