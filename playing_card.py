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
    def __init__(self, gameMode=None):
        self.deck = self.generateDeck(gameMode)

    @staticmethod
    def generateDeck(gameMode=None):
        # creating all cards 
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", \
            "8", "9", "10", "J", "Q", "K"]
        blackJack = {"A":1, "J":10, "Q":10, "K":10}
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i, value in enumerate(values):
                if gameMode == "21":
                    if value in blackJack.keys():
                        newDeck.append(Card(value, suit, (blackJack[value])))
                    else:
                        newDeck.append(Card(value, suit, int(value)))
                else:
                    newDeck.append(Card(value, suit, i + 1))
        
        # alternative way to write
        # for suit in suits:
        #    for i, value in enumerate(values):
        #        newDeck.append(Card(value, suit, (blackJack[value] if value in blackJack.keys() else int(value))\
        #            if gameMode == "21" else i+1))

        # code to debug
        # for card in newDeck:
        #    print(card.getCardString())

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
            "deck": Deck(gameMode)
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
    
    @staticmethod
    def winnerOf21(table):
        '''
        Function to show who win the game "21"
        1. calculate the score of each player by the function score21Individual
           and store the score to the list "points"
        2. calculate the number of the players for each score
           and store the number to the dictionary "cache"
        3. show the information below,
            a. if the number of the player of the maximum score
               (calculated by the function maxInArrayIndex in the class HelperFunctions)
               is more than 1, show "It is a draw".
            b. if the number is 1, show the winner
            c. otherwise, show "No winner..."
        '''
        points = []
        cache = {}
        for cards in table["players"]:
            point = Dealer.score21Individual(cards)
            points.append(point)
            if point in cache:
                cache[point] += 1
            else:
                cache[point] = 1
        
        print(points)

        winnerIndex = HelperFunctions.maxInArrayIndex(points)
        if cache[points[winnerIndex]] > 1:
            return "It is a draw"
        elif cache[points[winnerIndex]] > 0:
            return "player " + str(winnerIndex + 1) + " is the winner"
        else:
            return "No winners..."
        
    @staticmethod
    def checkWinner(table):
        if table["gameMode"] == "21":
            return Dealer.winnerOf21(table)
        else:
            return "no game"

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

table1 = Dealer.startGame(4, "21")
Dealer.printTableInformation(table1)
print(Dealer.checkWinner(table1))

table2 = Dealer.startGame(4, "poker")
Dealer.printTableInformation(table2)
print(Dealer.checkWinner(table2))