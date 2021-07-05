import random

def winnerPairOfCards(player1, player2):
    cards = Deck()
    cards.printDeck()
    return 1

class Card:
    '''
    Card: class for creating a card with below;
     value: any of "A", "2", "3", "4", "5", "6", "7", \
            "8", "9", "10", "J", "Q", "K"
     suit: any of "♣", "♦", "♥", "♠"
     strength: integer value to express the relationship below;
              2 < 3 < 4 < ... < 10 < J < Q < K < A
    '''
    def __init__(self, value, suit, strength):
        self.value = value
        self.suit = suit
        self.strength = strength
    
    def getCardString(self):
        return self.suit + self.value + "(" + str(self.strength) + ")"

class Deck:
    '''
    Deck: creating deck with all cards of playing card
    '''
    def __init__(self):
        self.deck = self.generateDeck()
    
    @staticmethod
    def generateDeck():
        newDeck = []
        values = ["2", "3", "4", "5", "6", "7", \
            "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♣", "♦", "♥", "♠"]
        
        for suit in suits:
            for i, value in enumerate(values):
                newDeck.append(Card(value, suit, i))
        
        return newDeck
    
    def printDeck(self):
        print("Displaying cards...")
        for card in self.deck:
            print(card.getCardString())
    
    def suffleDeck(self):
        deckSize = len(self.deck)
        for i in range(deckSize):
            j = random.randint(1, deckSize - 1)
            tmp = self.deck[i]
            self.deck[i] = self.deck[j]
            self.deck[j] = tmp
    
    def draw(self):
        return self.deck.pop()

card1 = Deck()
card1.suffleDeck()
card1.printDeck()



#winnerPairOfCards(1,2)
