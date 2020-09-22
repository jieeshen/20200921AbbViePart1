import random

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'clubs diamonds hearts spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        # this.dealer = dealer;   # 'this' is same as 'self'
        self.color = 'blue'
        self._make_deck()

        self.__foo = 'bar'


    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:  # why not CardDeck.SUITS?
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    # getter method
    def get_dealer(self):
        return self._dealer


    # getter property
    @property
    def dealer(self):
        return self._dealer.upper()


    # setter property
    @dealer.setter
    def dealer(self, value):  #  uses 'descriptors'
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer}, {len(self)})"

    def __add__(self, other):
        tmp = type(self)(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp

    def toString(self):
        return "wombat"



