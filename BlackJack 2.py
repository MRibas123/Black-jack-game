from random import shuffle
def deck():
    deck= []
    for suit in ['H', 'C', 'D', 'S']:
        for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'J', 'K']:
            deck.append(suit+value)
    shuffle(deck)
    return deck

def pontos(cartas):
    mypoint = 0
    acepoint= 0
    for i in cartas:
        if (i[1] == 'J' or i[1]== 'Q' or i[1]== 'K' or i[1] == '10'):
            mypoint += 10
        elif (i[1] != 'A'):
            mypoint += int(i[1])
        else:
            acepoint += 1

    if (acepoint == 1 and mypoint >= 10):
        mypoint += 11
    elif acepoint != 0:
        mypoint += 1
    return mypoint

def hands(deck):

    dealer_cards = []
    player_cards = []
    dealer_cards.append(deck.pop())
    dealer_cards.append(deck.pop())
    player_cards.append(deck.pop())
    player_cards.append(deck.pop())


    return [dealer_cards, player_cards]

game = ""
hands = hands(deck())
dealer = hands[0]
player = hands[1]
mydeck= deck ()
while game != "exit":
    print("Dealer has X and " + dealer [1])
    print("You have "+ str(player))


    if pontos(player) == 21:
        print("BLACKJACK! You won!")
        break
    elif pontos(player) >21:
        print("You have " + str(pontos(player)) +"! You have busted.")
        break
    elif pontos(dealer) > 21 :
        print("Dealer Busted with "+ str(pontos(dealer)) + "! You won.")
        break
    game = input("Would you like to hit your stand? h: to hit; s: to stand")
    if game == "h":
        player.append(mydeck.pop())
    elif pontos(player) > pontos(dealer):
        print("You win with " + str(pontos(player)) +"!")
        print("Dealer has: "+ str(dealer)+ ". With a total of "+str(pontos(dealer))+"!")
        break
    else:
        print("Dealer has: "+ str(dealer)+ ". With a total of "+str(pontos(dealer))+"!")
        print("Dealer Wins")
        break