# Guessing a Number game
from random import randint
import sys

settings = {"guess_amount": 5,
			"min_setting": 0,
			"max_setting": 20
			}


# generate random number to guess and only has 5 chances
def numGenerate(wins_counter=0):
	while True:
		# creates random number
		numAnswer = randint(settings["min_setting"], settings["max_setting"])
		print(numAnswer)

		guess_counter = 0
		user_number = int(input("Guess a number between 1-20: "))
		guess_counter += 1

		# guess amount reached check if player wants to play again by typing y, yes, n, and no. Case insensitive implemented
		if guess_counter == settings["guess_amount"]:
			print('Your win count currently is {}'.format(wins_counter))
			game_over = input("Game Over answer was {} would you like to try again?".format(numAnswer)).lower()
			if game_over.startswith('y'):
				numGenerate()
			elif game_over.startswith('n'):
				print("Thanks for playing!")
				sys.exit()

		# implement player decision to play again here
		if user_number == numAnswer:
			print('Correct you win with the correct guess of {}'.format(numAnswer))
			wins_counter += 1
			print("Win count is: {}".format(wins_counter))
			play_again = input("Would you like to play again? ".format(wins_counter))
			if play_again.startswith('y'):
				continue
			elif play_again.startswith('n'):
				print("Thanks for playing!")
				sys.exit()

		elif user_number != numAnswer:
			print('Wrong try again')

numGenerate()