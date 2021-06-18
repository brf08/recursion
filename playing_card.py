import random

class Card:
    '''
    Card: class for creating a card with below;
     value: any of "A", "2", "3", "4", "5", "6", "7", \
            "8", "9", "10", "J", "Q", "K"
     suit: any of "♣", "♦", "♥", "♠"
     intValue: integer for a specified value
    '''
    # constructor to generate instance
    def __init__(self, value, suit, intValue):
        self.value = value
        self.suit = suit
        self.intValue = intValue

    # function to show the state of an object
    def getCardString(self):
        return self.suit + self.value \
            + "(" + str(self.intValue) + ")"

class Deck:
    '''
    Deck: creating deck with all cards of playing card
    '''
    def __init__(self):
        self.deck = self.generateDeck()

    @staticmethod
    def generateDeck():
        # creating all cards 
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", \
            "8", "9", "10", "J", "Q", "K"]
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i, value in enumerate(values):
                #print(Card(value, suit, i + 1).getCardString())
                newDeck.append(Card(value, suit, i + 1))
        
        return newDeck
    
    def printDeck(self):
        # Function to show all cards in the deck
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

# Class for dealer (stateless object)
class Dealer:

    @staticmethod
    def startGame(amountOfPlayers, gameMode):
        # Info for the table
        table = {
            "players": [],
            "gameMode": gameMode,
            "deck": Deck()
        }

        # Suffle a deck
        table["deck"].suffleDeck()

        for person in range(0, amountOfPlayers):
            # define the list of the cards for each player
            playerCard = []
            # draw cards for each player based on the gameMode
            for i in range(0,Dealer.initialCards(gameMode)):
                playerCard.append(table["deck"].draw())
            table["players"].append(playerCard)
        
        #return the information for the table
        return table
    
    @staticmethod
    def initialCards(gameMode):
        # define how many cards each player should have
        if gameMode == "21":
            return 2
        if gameMode == "poker":
            return 5
    
    @staticmethod
    def printTableInformation(table):
        print("Amount of players: " + str(len(table["players"])) \
            + "... Game mode: " + table["gameMode"] \
                + ". At this table: ")

        # print the cards for each player
        for i, player in enumerate(table["players"]):
            print(str(i+1) + "player's cards: ")
            for card in player:
                print(card.getCardString())
    
    @staticmethod
    def score21Individual(cards):
        # calculate the sum of the intValue of the cards
        value = 0
        for card in cards:
            value += card.intValue
        # if the sum is more than 21 the player loses
        # so the score is set to 0
        return value if 21 >= value >= 1 else 0

class HelperFunctions:
    # the function that returns the index 
    # which value is the maximum in the array
    @staticmethod
    def maxInArrayIndex(intArr):
        maxIndex = 0
        maxValue = intArr[0]
        for i, num in enumerate(intArr):
            if num > maxValue:
                maxIndex = i
                maxValue = num

        return maxIndex

arr1 = [1, 9, 19, 3, 4, 6]
print(HelperFunctions. maxInArrayIndex(arr1))

arr2 = [5, 2, 1, 3, 5, 5]
print(HelperFunctions.maxInArrayIndex(arr2))