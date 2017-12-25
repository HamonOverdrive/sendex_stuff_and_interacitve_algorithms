import random

# notes about making card class and deck https://stackoverflow.com/questions/41970795/what-is-the-best-way-to-create-a-deck-of-cards
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value) + ' '+ str(self.suit)

    def getVal(self):
        return str(self.value)

values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']

# this creates the deck of 52 cards with all suits and values
deck = [Card(value, suit) for value in values for suit in suits]

# replaces player one value to number
def replaceValue(oneVal):
    if oneVal == 'A':
        oneVal = 1
        return oneVal
    elif oneVal == 'J':
        oneVal = 11
        return oneVal
    elif oneVal == 'Q':
        oneVal = 11
        return oneVal
    elif oneVal == 'K':
        oneVal = 12
        return oneVal
    else:
        pass

# replaces player two value to number
def replaceValue2(twoVal):
    if twoVal == 'A':
        twoVal = 1
        return twoVal
    elif twoVal == 'J':
        twoVal = 11
        return twoVal
    elif twoVal == 'Q':
        twoVal = 11
        return twoVal
    elif twoVal == 'K':
        twoVal = 12
        return twoVal
    else:
        pass

def main():
    letterList = ['A', 'J', 'Q', 'K']

    player1 = random.choice(deck)
    player2 = random.choice(deck)

    oneVal = player1.getVal()
    twoVal = player2.getVal()

    # calls function to turn rank value into number so it will be comparable to other number
    if oneVal in letterList:
        oneVal = replaceValue(oneVal)
    if twoVal in letterList:
        twoVal = replaceValue2(twoVal)

    # checks player one and player two draw
    print('Player 1 draws: {}'.format(player1))
    print('Player 2 draws: {}'.format(player2))

    # checks winner or draw
    if int(oneVal) > int(twoVal):
        print('Player 1 wins')
    elif int(twoVal) > int(oneVal):
        print('Player 2 wins')
    else:
        print('Draw keep your money')

main()
