from random import *
from player import Player
from deck import Deck
from deck import Card

class Game(object):
    def __init__(self,players):
        self.gameName="Go_Fish"
        self.playersNum=players
        self.players=[]
        self.player_create()
        self.deck=Deck()
    # def Ask(self,player,ask):
    #     temp=[]
    #     for card in player.hand:
    #         if card.value == ask:
    #             del card.value
    #             temp.append(card)
    #         if len(temp)!=0:
    #             player.hand.append(temp)
    def player_create(self):
        for i in range(1,self.playersNum+1):
            self.players.append(Player(i))
        print self.players
        return self
    def first_turn(self):
        x=randint(0,self.playersNum)
        vall=self.players[x].play()
        return self

test=Game(4)
Deck().build()
test.first_turn()