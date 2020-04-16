import random

# Snakes and Ladders dictionary
SnLadDict = {
		  7: 18,
          16: 3,
          22: 15,
          26: 21,
          35: 44,
          39: 35,
          46: 62,
          67: 58,
          70: 58,
          78: 69,
          85: 86,
          86: 81,
          88: 30,
		  92: 55,
		  99: 2
        }


# Player class
class SnakeLadder:
	def __init__(self, inPlayerNum):
		self.playerPos = 0
		self.playerNum = inPlayerNum

	def updatePosition(self, inPos):
		self.playerPos = inPos

	def getPosition(self):
		return self.playerPos

	def getPlayerNum(self):
		return self.playerNum

# Program entrance
if __name__ == '__main__':
	global winner
	winner = False
	numPlayers = int(input('Enter number of players: '))

	# If only one player is playing ,then second player is computer
	if numPlayers == 1 :
		numPlayers+=1
	else:
		numPlayers

	for i in range(0,numPlayers):
		playerList.append(SnakeLadder(i + 1))