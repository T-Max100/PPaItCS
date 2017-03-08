from random import choice
#import pdb

D = tuple(range(1,11))

"""
def main():
	ans = printIntro()
	result = dealGame(ans)
	printEnd(result)

def printIntro():
	input("Play a game of blackjack (y/n)? ")

def dealGame(ans):
	dealerHand = userHand = []
	if ans in {"y", "Y", "yes", "Yes", "YES"}:
		for i in range(2):
			dealerHand.append(choice(D))
			userHand.append(choice(D))
		if (1 in dealerHand and sum(dealerHand) == 11) and (1 in userHand and sum(userHand) == 11):
			return "Both Win!"
		elif (1 in userHand and sum(userHand) == 11):
			return "User Wins!"
		elif (1 in dealerHand and sum(dealerHand) == 11):
			return "Dealer Wins!"
		else:
			return blackjack(dealerHand, userHand)
	else:
	return "uninterested"

def blackjack(dealerHand, userHand):
	hasAce = False
	while sum(dealerHand) < 17:
		if 1 in dealerHand and sum(dealerHand) > 5:
			hasAce = True
			dealerHand[dealerHand.index(1)] = 11
		else:
			dealerHand.append(choice(D))
	while sum(userHand) <= 21:
		ans = input("Hit? ")
		if ans in {"y", "Y", "yes", "Yes", "YES"}:
			userHand.append(choice(D))
			print(sum(userHand))
		else:
			if (sum(dealerHand) <= sum(userHand) <= 21) or (sum(dealerHand) > 21):
				return "User Wins!"
			else:
				return "Dealer Wins!"

def printEnd(result):
	print(result)
"""

def main():
	ans = printIntro()
	result = dealDealerHand(ans)
	printEnd(result)

def printIntro():
	ans = input("Play a game of blackjack (y/n)? ")
	return ans

def dealDealerHand(ans):
	dealerHand = []
	userHand = []
	if ans in {"y", "Y", "yes", "Yes", "YES"}:
		while sum(dealerHand) < 17:
			nextCard = choice(D)
			dealerHand.append(nextCard)
			print(dealerHand)
		resultD = blackjackD(dealerHand)
		resultU = blackjackU(userHand)
		result = [resultD, resultU]
	else:
		result = "uninterested"
	return result

def blackjackD(dealerHand):
	if 1 in dealerHand:
		hasAce = True
	else:
		hasAce = False
	if hasAce and 6 <= sum(dealerHand) <= 11:
		dealerHand[dealerHand.index(1)] = 11
	if (hasAce and sum(dealerHand) == 11):
		print(dealerHand)
		print(sum(dealerHand))
		result = "Dealer Wins!"
	elif sum(dealerHand) > 21:
		print(dealerHand)
		print(sum(dealerHand))
		result = "User Wins!"
	else:
		result = dealerHand
	return result

def blackjackU(userHand):
	for i in range(2):
		userHand.append(choice(D))
	print(userHand)
	if 1 in userHand:
		hasAce = True
	else:
		hasAce = False
	print(sum(userHand))
	if hasAce:
		print("Has Ace")
	ans = input("Hit? ")
	while ans in {"y", "Y", "yes", "Yes", "YES"}:
		print(sum(userHand))
		userHand.append(choice(D))
		print(sum(userHand))
		if hasAce and 6 <= sum(userHand) <= 11:
			userHand[userHand.index(1)] = 11
		elif (hasAce and sum(userHand) == 11):
			print(userHand)
			print(sum(userHand))
			result = "User Wins!"
			break
		ans = input("Hit? ")
	if sum(userHand) > 21:
		print(userHand)
		print(sum(userHand))
		result = "Dealer Wins!"
	else:
		result = userHand
	return result

def printEnd(result):
	#pdb.set_trace()
	if result == "uninterested":
		end = print("uninterested")
	elif result[0] == result[1]:
		end = print(result[0])
	elif type(result[0]) == str and type(result[1]) != str:
		end = print(result[0])
	elif type(result[1]) == str and type(result[0]) != str:
		end = print(result[1])
	elif type(result[0]) == str and result[0] != result[1]:
		end = "No Winner!"
	else:
		D = sum(result[0])
		U = sum(result[1])
		print("Dealer had {} which adds up to {}".format(result[0], D))
		print("User had {} which adds up to {}".format(result[1], U))
		if D == U:
			end = print("No Winner!")
		elif max(D,U) == D:
			print(result[0])
			print(D)
			end = print("Dealer Wins!")
		else:
			print(result[1])
			print(U)
			end = print("User Wins!")
	return end

if __name__ == '__main__': main()
