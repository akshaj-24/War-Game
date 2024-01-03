"""
War Card Game:
How to Play:


For more info refer to: https://en.wikipedia.org/wiki/War_(card_game)

Created by AKSHAJ
"""
from typing import Any

winner=False

# Importing the random library to shuffle cards
import random

# Creating Global Variables
suits=("Clubs","Diamonds","Hearts","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,
        "Queen":12,"King":13,"Ace":14}

# Creating classes
class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                rank_suit=Card(suit,rank)
                self.all_cards.append(rank_suit)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player: {self.name} has {len(self.all_cards)} cards"

playerOne=Player("One")
playerTwo=Player("Two")
new_deck=Deck()
new_deck.shuffle()

#Dealing cards
for i in range(26):
    playerOne.add_cards(new_deck.deal_one())
    playerTwo.add_cards(new_deck.deal_one())

def win(player):
    global winner
    if len(player.all_cards)==0:
        winner=True
    return winner

def declareWinner():
    if len(playerOne.all_cards)<3:
        print('Player Two WINS')
    elif len(playerTwo.all_cards)<3:
        print("Player One WINS")
    else:
        print('Failure in Declaring Winner')

roundnum=0

while winner==False:
    roundnum+=1
    print(f"Round {roundnum}")

    one_current_cards=[]
    one_current_cards.append(playerOne.remove_one())
    two_current_cards=[]
    two_current_cards.append(playerTwo.remove_one())


    atWar=True
    while atWar:
        if (one_current_cards[-1].value)>(two_current_cards[-1].value):
            playerOne.add_cards(one_current_cards)
            playerOne.add_cards(two_current_cards)
            atWar=False
        elif two_current_cards[-1].value>one_current_cards[-1].value:
            playerTwo.add_cards(one_current_cards)
            playerTwo.add_cards(two_current_cards)
            atWar=False
        else:
            print("WAR! WAR! WAR!")
            if len(playerOne.all_cards)<3:
                print("Player One unable to declare WAR")
                winner=True
                break
            elif len(playerTwo.all_cards)<3:
                print("Player Two unable to declare WAR")
                winner=True
                break
            else:
                for i in range(3):
                    one_current_cards.append(playerOne.remove_one())
                    two_current_cards.append(playerTwo.remove_one())

    win(playerOne)
    win(playerTwo)

declareWinner()
