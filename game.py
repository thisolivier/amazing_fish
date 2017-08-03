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
        self.deal()
        self.first_turn()
        
    # def Ask(self,player,ask):
    #     temp=[]
    #     for card in player.hand:
    #         if card.value == ask:
    #             del card.value
    #             temp.append(card)
    #         if len(temp)!=0:
    #             player.hand.append(temp)
    def deal(self,deal=7):
        for i in range(0,deal):
            for x in range(0,self.playersNum):
                cardDraw=self.deck.cards.pop()
                self.players[x].draw(cardDraw)
        return self
    def player_create(self):
        for i in range(1,self.playersNum+1):
            self.players.append(Player(i))
        print self.players
        return self
    def first_turn(self):
        x=randint(0,self.playersNum)
        vall=self.players[x].play()
        temp=[]
        for card in vall[1].hand:
            if card.value == vall[0]:
                del card.value
                temp.append(card)
            if len(temp)!=0:
                self.players[x].hand.append(temp)
        return self

if __name__ == "__main__":

    test=Game(4)


