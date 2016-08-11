''' This is a program that models a tournament of rock, paper, scissors between a computer
and human player. Some of the functions have been written for you but the rest need to be
filled in where it says your code goes here!'''

#declare constants for the program
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
HUMAN = "human"
COMPUTER = "computer"
TIE = "tie"
import random
'''This function models a turn by a human player. It should allow a human to choose a move and
	return that move.
	Input: None
	Output: ROCK, PAPER, or SCISSORS'''
def human_turn():
	answer=input("ROCK,PAPER,SCISSORS?")
	return answer

'''This function models a turn by a human player. It should allow a computer to randomly select a move
	and return that move.
	Input: None
	Output: ROCK, PAPER, or SCISSORS'''
def computer_turn():
	choices=[ROCK,PAPER,SCISSORS]
	comp_length=len(choices)
	comprand=random.randint(0,comp_length-1)
	compchoice=choices[comprand]
	return compchoice

'''This function models a turn by a human player. It should allow a computer to randomly select a move
	and return that move.
	Input: player1's move, player2's move
	Output: HUMAN, TIE, or COMPUTER'''
def determine_winner(player1, player2):
	if player1 == ROCK:
		if player2 == ROCK:
			return TIE
		if player2 == PAPER:
			return COMPUTER
		if player2 == SCISSORS:
			return HUMAN
	elif player1 == PAPER:
		if player2 == ROCK:
			return HUMAN
		elif player2 == PAPER:
			return TIE
		elif player2 == SCISSORS:
			return COMPUTER
	else:
		if player2 == ROCK:
			return COMPUTER
		elif player2 == PAPER:
			return HUMAN
		elif player2 == SCISSORS:
			return TIE


'''This function plays a single round of rock, paper, scissors. It should give the human player a turn, the
	computer player a turn, and determine a winner.
	Input: None
	Output: victorious player (HUMAN, COMPUTER, or TIE)'''
def play_round():
	player1=human_turn()
	player2=computer_turn()
	return determine_winner(player1, player2)


'''This function models multiple rounds of rock, paper, scissors. It can keep track of each player's
	score and the tournament ends when a player reaches a score of 10. For ease of viewing the current
	score is printed after each round.
	Input: None
	Output: Winner's score'''
def play_tournment():
	#set up score variables
	human_score = 0
	computer_score = 0

	#while the game is not over play another round
	while computer_score < 10 and human_score < 10:
		win = play_round()

		#scores the round and increments the winner's score
		if win == HUMAN:
			human_score += 1
		elif win == COMPUTER:
			computer_score += 1
		print("Human Score: " + str(human_score) + " Computer Score: " + str(computer_score))
	return max(computer_score, human_score)


#runs the single function play_tournment
play_tournment()
