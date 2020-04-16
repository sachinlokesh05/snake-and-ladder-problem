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

# Function to handle the players turn
def gameWinner(inPlayer):
	global winner
	# check for game winner
	if inPlayer.getPosition() == 100:

		# If Computer is the Winner
		if numPlayers == 2 and inPlayer.playerNum == 1:
			print("Computer is the Winner!")
			winner = True
		else:
			print("Player %i is the Winner!" % inPlayer.getPlayerNum())
			winner = True

	# run dice rolls and movements
	if winner == False:
		print("\n----Player %i Hit enter to roll----" % inPlayer.getPlayerNum())
		# Uncomment to require space to be pressed before jumping turns
		# input()
		roll = rollDice()
		print("You rolled: %i" % roll)
		movePlayer(inPlayer, roll)
		checkPosition(inPlayer)

# Function to return the Integer value of a 6 side dice roll
def rollDice():
    return random.randint(1,6)

# Handle player movements
def movePlayer(inPlayer, roll):
	if inPlayer.getPosition() + roll <= 100:
		inPlayer.updatePosition(inPlayer.getPosition() + roll)
		print("You are at spot %i" % inPlayer.getPosition())
	else:
		print("You rolled too far")


# Checks player landing position and adjusts if snake or ladder
def checkPosition(inPlayer):
	for pos in SnLadDict:
		if pos == inPlayer.getPosition():
			if pos < SnLadDict[pos]:
				print("You climbed a Ladder to spot %i" % SnLadDict[pos])
			else:
				print("You rode a Snake to spot %i" % SnLadDict[pos])
			inPlayer.updatePosition(SnLadDict[pos])

# Program entrance
if __name__ == '__main__':
	global winner
	winner = False
	numPlayers = int(input('Enter number of players: '))
	playerList = []

	# If only one player is playing ,then second player is computer
	if numPlayers == 1 :
		numPlayers+=1
	else:
		numPlayers

	for i in range(0,numPlayers):
		playerList.append(SnakeLadder(i + 1))

	while winner == False:
		for i in playerList:
			if winner == False:
				gameWinner(i)