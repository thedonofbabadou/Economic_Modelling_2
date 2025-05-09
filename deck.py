import random


class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)


class Deck:
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return ", ".join(map(str, self.cards))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("No more cards to deal")
        return self.cards.pop(0)


if __name__ == "__main__":
    c1 = Card("A", "♣")
    print(f"Card created: {c1}")

    deck = Deck()
    print("Deck before shuffling:")
    print(deck)

    deck.shuffle()
    print("\nDeck after shuffling:")
    print(deck)

    print("\nDealing a card:")
    print(deck.deal())

    print("\nRemaining deck:")
    print(deck)
