from random import shuffle
class Deck(object):
    def __init__(self):
        self.size=52
        self.cards=[]
        self.suits=["hearts","clubs","dimonds","spades"]
        self.build()
        self.shuffle()

    def __repr__(self):
        for card in self.cards
            print card

    def build(self):
        cards_in_suit=(self.size/len(self.suits))
        
        for x in range(0,len(self.suits)):
            for i in range(1,cards_in_suit+1):
                self.cards.append(Card(i,self.suits[x]))
            print "build is working!"
        return self

    def shuffle(self):
        shuffle(self.cards)
        print "shuffle is working!"
        return self 
        
class Card(object):
    def __init__(self,value,suit):
        self.suit=suit
        self.value=value
    def __repr__(self):
        return "<Card val {} suit {}>".format(self.value, self.suit)