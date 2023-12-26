import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()

print(len(deck))
print(deck[0])
print(deck[-1])

# works because __getitem__ is implemented
print(choice(deck))

# because out __getitem__ delegates to the [] operator of self._cards
# it supports slicing
print(deck[:3])
print(deck[12::13])

# and it also support iteration
for card in deck:
    print(card)

# and sorting
    suit_values = dict(spades=2, hearts=3, diamonds=4, clubs=1)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
    
    for card in sorted(deck, key=spades_high):
        print(card)