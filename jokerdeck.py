from carddeck import CardDeck

class Game:

    def play(self):
        print("playing...")

class JokerDeck(CardDeck, Game):
    def _make_deck(self):
        super()._make_deck(self)

        self._cards.append('Joker1')
        self._cards.append('Joker2')
