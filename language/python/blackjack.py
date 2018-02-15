import random, unittest


class Card:
    def __init__(self, rank, suit='spades'):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '%s %s' % (self.suit, self.rank)

    def __repr__(self):
        return self.__str__()

    def is_number(self):
        return self.rank not in list('JQKA')

    def is_face(self):
        return self.rank in list('JQK')

    def is_ace(self):
        return self.rank == 'A'

    def get_point(self):
        if self.is_number():
            return int(self.rank)
        elif self.is_face():
            return 10
        else:
            return 11

    def get_min_point(self):
        return 1 if self.is_ace() else self.get_point()


class Hand(list):
    def __str__(self):
        s = '%s,%s points' % (super().__str__(), self.get_points())
        if self.is_bust():
            s += ',bust'
        if self.is_blackjack():
            s += ',blackjack'
        return s

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

    def is_blackjack(self):
        return len(self) == 2 and self.get_points() == 21

    def allow_draw(self):
        return not self.is_bust() and len(self) < 5


class TestBlackjack(unittest.TestCase):
    def test_card(self):
        self.assertEqual(2, Card(2).get_point())
        self.assertEqual(10, Card('J').get_point())
        self.assertEqual(11, Card('A').get_point())
        self.assertTrue(Card(2).is_number())
        self.assertFalse(Card('J').is_number())
        self.assertFalse(Card('A').is_number())

    def test_hand(self):
        self.assertEqual(2, Hand([Card(2)]).get_points())
        self.assertEqual(10, Hand([Card('J')]).get_points())
        self.assertEqual(11, Hand([Card('A')]).get_points())
        self.assertEqual(13, Hand([Card(2), Card('A')]).get_points())
        self.assertEqual(14, Hand([Card(2), Card('A'), Card('A')]).get_points())
        self.assertEqual(15, Hand([Card(2), Card('A'), Card('A'), Card('A')]).get_points())
        self.assertEqual(23, Hand([Card(2), Card('J'), Card('J'), Card('A')]).get_points())
        self.assertEqual(15, Hand([Card(2), Card('A'), Card('A'), Card('A'), Card(10)]).get_points())
        self.assertEqual(24, Hand([Card(2), Card('A'), Card('A'), Card(10), Card(10)]).get_points())
        self.assertTrue(Hand([Card(2), Card('A'), Card('A'), Card('A')]).allow_draw())
        self.assertFalse(Hand([Card(2), Card('J'), Card('J'), Card('A')]).allow_draw())
        self.assertFalse(Hand([Card(2), Card('A'), Card('A'), Card('A'), Card(10)]).allow_draw())


# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    hand = Hand()

    hand.append(deck.pop())
    hand.append(deck.pop())

    print(hand)
    while hand.allow_draw() and len(deck) > 0 and input('draw (y/n)?') == 'y':
        hand.append(deck.pop())
        print(hand)
    print('over')

"""
goal:
    a blackjack cmd game = a practice to master python basics
flow:
    shuffle deck
    hand = deck.pop 2
    while hand.allowDraw and deck.allowDraw and user.draw:
        hand <- deck.pop 1
todo:
    - [x] hello blackjack 0.5h

    - [x] Hand.get_points() 1h
    - [x] impl handAllowDraw 0.1h
    
    - [x] fix point rule 0.5h
    - [x] adapt main 0.5h
"""
