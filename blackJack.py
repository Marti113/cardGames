import random

#Jack Queen King are 10 points
fullDeck = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4}

#maybe needs deck, or players passed in?
def play(deck):

    player1 = 0
    player2 = 0

    while(player1 < 21 and player2 < 21):
        print(player1, player2)
        player1 = hit(player1, deck)
        player2 = hit(player2, deck)
    
    if(player1 < player2):
        print('Player1 Wins!')
    else:
        print('Player2 Wins!')

#returns a number from the 'deck' dictonary
def hit(player, deck):

    print(list(deck))
    returnCard = random.choice(list(deck))
  
    cardsLeft = deck[returnCard]
    
    ##player is awarded the points
    ##card needs to be taken out of the deck
    player += returnCard
    cardsLeft -= 1
    if(cardsLeft == 0):
        del deck[returnCard]
    else:    
        deck[returnCard] = cardsLeft
    return player
        
play(fullDeck)







    
    