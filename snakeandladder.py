import random

# Player class
class Player:
	def __init__(self, inPlayerNum):
		self.playerPos = 1
		self.playerNum = inPlayerNum

# Program entrance
if __name__ == '__main__':
	global winner
	winner = False
	numPlayers = int(input('Enter number of players: '))
