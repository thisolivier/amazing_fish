class Player(object):
    def __init__ (self, playerNo):
        self.name = "Player {}".format(playerNo)
        self.cards = {} 

    def play (self):
        print "\n---------\nYou are {}, your hand contains:".format(self.name)
        listHand = []
        for key in self.cards:
            suit = self.cards[key].suit
            value = self.cards[key].value
            listHand.append(key)
            print "{}) {} of {}".format(len(listHand), value, suit)
        which = input("\nWhich value do you want to check for?") -1
        whichPlayer = input("\nWhich player are you asking?")
        requestVal = self.cards[listHand[which]].value
        returnVal = [requestVal, whichPlayer]
        return returnVal
    
    def draw (self, card):
        keyName = str(card.value) + str(card.suit)
        print "Adding card, keyname ",keyName
        print "The card is ",card
        self.cards[keyName] = card
        return self

    def ask (self, val):
        returnVal = []
        for key in self.cards:
            if cards[key].value == val:
                returnVal.append(self.cards[key])
        if len(returnVal) == 0 : returnVal = False
        return returnVal