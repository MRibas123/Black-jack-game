from enum import IntEnum
from enum import Enum
from random import *

class Value(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11

class Suit(Enum):
    SPADE = 'spades'
    HEARTS = 'hearts'
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'

class cartas_jogadas:
    def __init__(self, card_value, card_suit):
        self.value = card_value
        self.suit= card_suit

full_deck = []
partial_deck = []
def create_deck():
    for suit in Suit:
        for value in Value:
            full_deck.append(cartas_jogadas(Value(value), Suit(suit)))
        return full_deck

def draw_card(deck):
    rand_card = randint(0, len(deck) - 1)
    return deck.pop(rand_card)

dealer_cards = []
player_cards = []

create_deck()
partial_deck = list(full_deck)

test_card = draw_card(partial_deck)


while len(dealer_cards) != 2:
    dealer_cards.append(draw_card(partial_deck))
    if len(dealer_cards) == 2:
        print("Dealer has X and " + str(dealer_cards[1].value) +" "+ str(dealer_cards[1].value) )


