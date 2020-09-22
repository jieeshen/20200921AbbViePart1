
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Tom')
d2 = CardDeck('Susan')

print(d1, d2)

print(d1.get_dealer())

print(d1.dealer)

print(d1.color)

d1.color = "chartreuse"

d1.dealer = 'Jeff'

print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)
print()

for i in range(5):
    print(d1.draw())
print()

x = d1.draw()
x = CardDeck.draw(d1)

print(d1.get_suits())
CardDeck.get_suits()

j1 = JokerDeck("Jimmy")
j2 = JokerDeck("Jane")

print(j1)
j1.shuffle()
print(j1.draw())
print(j1.cards)
j1.play()

print(JokerDeck.mro())

print(d1._cards[0])  # NAUGHTY!!
