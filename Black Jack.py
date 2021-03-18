import random
import numpy as np


baralho = [
  # 2  3  4  5  6  7  8  9  10  J   Q   K   A
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]
dealer_cards = []
player_cards = []

#Cartas iniciais do Dealer
while len(dealer_cards) != 2:
    dealer_cards.append(random.choice(baralho))
    if len(dealer_cards) == 2:
        print("Dealer tem X & " + str(dealer_cards[1]))

#Cartas iniciais do jogador
while len(player_cards) != 2:
    player_cards.append(random.choice(baralho))
    if len(player_cards) == 2:
        print("Player tem " + str(player_cards) + " com um total de " + str(sum(player_cards)))

#Jogo

while sum(player_cards) <= 21:
    action = input("Do you want to stay or hit? ")
    if action == "y":
        player_cards.append(random.choice(baralho))
        print("Player " + str(player_cards) +" with a total of " + str(sum(player_cards)))
    elif action == "n":
        print("You have a total of " + str(sum(player_cards)) + " with the cards " + str(player_cards))
        break
while sum(dealer_cards) < 16:
        dealer_cards.append(random.choice(baralho))
        print("Dealer has a total of " + str(sum(dealer_cards)) + " with the cards " + str(dealer_cards))
        if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) <= 21:
            print("Dealer wins! Dealer has a total of " + str(sum(dealer_cards)) + " with the cards " + str(dealer_cards))
        elif sum(dealer_cards) > 21:
            print("Dealer Busted! You Win! Dealer has a total of " + str(sum(dealer_cards)) + " with the cards " + str(dealer_cards))
        elif sum(dealer_cards) == sum(player_cards):
            print("Empate! Dealer has a total of " + str(sum(dealer_cards)) + " with the cards " + str(dealer_cards))
        elif sum(dealer_cards) == 21 and sum(dealer_cards) > sum(player_cards):
            print("Dealer has 21 and Wins! Dealer has a total of " + str(sum(dealer_cards)) + " with the cards " + str(dealer_cards))
        elif sum(dealer_cards) < sum(player_cards) and sum(player_cards) < 22:
            print("You win!Dealer has a total of " + str(sum(dealer_cards)) + " with the cards " + str(dealer_cards))
        elif sum(player_cards) == 21 and sum(dealer_cards) < sum(player_cards):
            print("You have BlackJack. You win!")
            break





