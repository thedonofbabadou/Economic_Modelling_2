from CardDeck import Deck, Card


class Hand:
    """
    Represents a hand of 5 cards drawn from a deck.
    """
    def __init__(self, deck):
        if not isinstance(deck, Deck):
            raise ValueError("Expected a Deck instance")
        if len(deck.cards) < 5:
            raise ValueError("Not enough cards in the deck to draw a hand")
        self._hand = [deck.deal() for _ in range(5)]

    @property
    def hand(self):
        return self._hand

    def __str__(self):
        return ', '.join(map(str, self.hand))

    @property
    def is_flush(self):
        return len(set(card.suit for card in self.hand)) == 1

    @property
    def num_matches(self):
        ranks = [card.rank for card in self.hand]
        return sum(ranks.count(rank) - 1 for rank in set(ranks))

    @property
    def is_pair(self):
        return self.num_matches == 2

    @property
    def is_2pair(self):
        return self.num_matches == 4

    @property
    def is_trip(self):
        return self.num_matches == 6

    @property
    def is_full(self):
        return self.num_matches == 8

    @property
    def is_quad(self):
        return self.num_matches == 12

    @property
    def is_straight(self):
        sorted_hand = sorted(self.hand, key=lambda card: Card.RANKS.index(card.rank))
        for i in range(1, 5):
            if Card.RANKS.index(sorted_hand[i].rank) != Card.RANKS.index(sorted_hand[i - 1].rank) + 1:
                return False
        return True


# Simulation to find straights
count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        matches += 1

print(f"Probability of getting a straight: {100 * (matches / count):.2f}%")
