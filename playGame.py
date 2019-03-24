import pydealer

def dealDeck(deck, st):
	# Deal a card to each column
	for s in st:
		card = deck.deal()
		s.append(card)
	return [ deck, st ]

def moveCards(s):
	# Initialize necessary variables
	canMove = True
	emptyCols = []
	availCols = []
	highVal = 0
	lowVal = 13
	suitMatch = False
	ideal = False
	# We are in the move cards algorithm, so check which columns are are empty
	# and which columns have cards to give
	
	for col in s:
		if(len(col) == 0):
			emptyCols.append(col)
		elif(len(col) > 1):
			availCols.append(col)
			val = col[len(col)-1].ranks.values()[0][col[len(col)-1].cards[0].value]
			suit1 = col[len(col)-1].cards[0].suit
			suit2 = col[len(col)-2].cards[0].suit
			val2 = col[len(col)-2].ranks.values()[0][col[len(col)-2].cards[0].value]
			if(suit1 == suit2):
				suitMatch = True
				if(val < val2):
					sameSuitIndex = availCols.index(col)
					ideal = True
				if(not ideal):
					sameSuitIndex = availCols.index(col)
			if(val < lowVal):
			#	print "val: " + str(val)
			#	print "low val: "+str(lowVal)
				lowVal = val
				lowestIndex = availCols.index(col)
#				print "lowest Index: " + str(lowestIndex)
			if(val > highVal):
				highestVal = val
				highestIndex = availCols.index(col)

	# Option 1: Move whatever is the lowest card first.
	# Commented out because it was found to be less effective than options 1 and 2 after testing
	# if(lowVal != 13 and not suitMatch):
	# 	card = availCols.pop(lowestIndex).pop()
		# emptyCols.pop().append(card)

	# Option 2: Move whatever is the highest card first.
	if(highVal != 0 and not suitMatch):
		card = availCols.pop(highestIndex).pop()
		emptyCols.pop().append(card)

	# # Option 3: Check the card directly beneath, and give priority if it is of the same suit 
	if(suitMatch):
	  	card = availCols.pop(sameSuitIndex).pop()
	  	emptyCols.pop().append(card)

	for avail in availCols:
		if(emptyCols):
			card = avail.pop()
			emptyCols.pop().append(card)
	return s

def removeCards(st):
	canRemove = True
	while(canRemove):
		# Loop through the cards and remove any cards that are lower.
		# First Loop, represents the first column we are comparing against
		for f in st:
			# Second loop, represents the column we are comparing with
			for s in st:
				# We need to ensure that both columns still have space so we 
				# don't try to pop off of an empty column
				if(len(s) > 0 and len(f) > 0 ):
					# We need to pull the first card off of both stacks in the inner loop
					# to ensure we don't accidentally pop off a card underneath a card that just got
					# popped
					card1 = f[len(f)-1]
					# We need to access the "ranks" dictionary to convert face cards to an int
					value1 = card1.ranks.values()[0][card1.cards[0].value]
					suit1 = card1.cards[0].suit
					card2 = s[len(s)-1]
					value2 = card2.ranks.values()[0][card2.cards[0].value]
					suit2 = card2.cards[0].suit
					if(value1 < value2 and suit1 == suit2):
						f.pop()
						continue
		
		# Check to see if we can move any cards - we need a column that is empty
		# and a column that has more than one card for this to be the case. 
		# if columns are empty but there are no available cards, then we deal again.
		# Otherwise, we move the cards. 
		zeroes = False
		available = False
		for col in st:
			if(len(col) == 0):
				zeroes = True
			if(len(col) > 1):
				available = True

		if(zeroes and not available):
			canRemove = False
			continue

		if(zeroes and available):
			st = moveCards(st)
			continue

		# Check to see if there are 4 different suits present in the stacks. If there are, we can no 
		# longer remove any cards and we will stop.
		suitCheck = set()
		for f in st:
			if(len(f) > 0):
				suitCheck.add(f[len(f)-1].cards[0].suit)
		if(len(suitCheck) == 4):
			canRemove = False
	return st

def main():
	# Initialize win counter
	win = 0
	for i in range(10000):
		# We need to reset the 4 columns and the stack every time we begin a new game
		c1 = []
		c2 = []
		c3 = []
		c4 = []
		stack = [c1, c2, c3, c4]

		# Initialize and shuffle a deck
		deck = pydealer.Deck()
		deck.shuffle()
		while(deck):
			# Make sure we set the stack and deck to their post-deal values
			arr = dealDeck(deck,stack)
			deck = arr[0]
			stack = arr[1]
			# Remove the cards appropriately
			removeCards(stack)
		
		# Calculate our final score by checking how many cards are still in play
		score = 0
		for cols in stack:
			score += len(cols)

		# If there are only 4 cards left, then we've won.
		if(score == 4):
			for cols in stack:
				print cols
			print "Win after " + str(i) + " games"
			win += 1

	# Print the final result
	print "Of 10,000 games, " + str(win) + " were wins."

if __name__ == "__main__":
    main()

