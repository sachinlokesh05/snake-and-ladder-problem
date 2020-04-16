import random

# Player class
class Player:
	def __init__(self, inPlayerNum):
		self.playerPos = 1
		self.playerNum = inPlayerNum


# Function to return the Integer value of a 6 side dice roll
def rollDice():
    return random.randint(1,6)
	
# Program entrance
if __name__ == '__main__':
	global winner
	winner = False
	numPlayers = int(input('Enter number of players: '))
