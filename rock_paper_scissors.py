#Rock, paper, scisscors game
#4.10.21
#ruthlesscattle

#Imports time module and choice function from random module
#I imported the time module as I wanted to introduce a slight delay with the gameplay loop 
import time
from random import choice

#List of 'hand' shapes that user/computer can choose
shapes = ['rock','paper','scissors']

#Prompt for user's choice of shape
choice_prompt = "\nWhat are you going with? "
choice_prompt += shapes[0].title() + ", " + shapes[1].title() + " or " + shapes[2].title() + "? "

def rock_paper_scissors_callout():
	"""Function that prints the 'players' calling out the name of the 'shapes'"""
	print("\nHere we go...\n\nRock!")
	time.sleep(1)
	print("\nPaper!")
	time.sleep(1)
	print("\nScisssors!")
	time.sleep(1)
	print(f"\nComputer chose... {computer_choice.title()}!")
	time.sleep(1)

def win_scenarios():
	"""Function that checks to see if user or computer wins game"""
	if user_choice_input == 'rock' and computer_choice == 'paper':
		print("\nPaper covers Rock... you lose!\n")
	elif user_choice_input == 'paper' and computer_choice == 'rock':
		print("\nPaper covers Rock... you win!\n")
	elif user_choice_input == 'rock' and computer_choice == 'scissors':
		print("\nRock crushes Scissors... you win!\n")
	elif user_choice_input == 'Scissors' and computer_choice == 'rock':
		print("\nRock crushes Scissors... you lose!!\n")
	elif user_choice_input == 'paper' and computer_choice == 'scissors':
		print("\nScissors cuts Paper... you lose!\n")
	elif user_choice_input == 'scissors' and computer_choice == 'paper':
		print("\nScissors cuts Paper... you win!\n")

#Main gamelay loop
while True:
	#Using choice function from random module to pick a shape for computer opponent.
	computer_choice = choice(shapes)
	#User input to see if user wants to play the game
	new_game = input("Do you want to play Rock Paper Scissors? (yes/no) ")
	#Converts user's input to lowercase, in case of choice capitlisation. Also strips any accidental whitespace.
	new_game = new_game.lower()
	new_game = new_game.strip()
	if new_game == 'y' or new_game == 'yes':
		user_choice_input = input(choice_prompt)
		#Converts user's input to lowercase, in case of choice capitlisation. Also strips any accidental whitespace.
		user_choice_input = user_choice_input.lower()
		user_choice_input = user_choice_input.strip()
		#If user chooses/enters shape not in shapes list, prints error and restarts while loop
		if user_choice_input not in shapes:
			print("That is not a valid entry!")
			continue
		#Checks to see if user's shape choice and computer's shape is the same, in which case it is a tie.
		elif computer_choice == user_choice_input:
			rock_paper_scissors_callout()
			print(f"\nIt's a tie! You both chose {user_choice_input.title()}!\n")
			continue
		#If user has input valid entries/data, gameplay function is called to see who wins the game.
		else:
			rock_paper_scissors_callout()
			win_scenarios()
			#After game, restarts while loop to see if user wants to continue playing.
			continue
	#If user enters n or no, game/application ends
	elif new_game == 'n' or new_game == 'no':
		break
	#If user enters q or quit, game/application ends
	elif new_game == 'q' or new_game == 'quit':
		break
	#If user enters anything other than y/yes, n/no or q/quit, prints error message and restarts while loop
	else:
		print("That is not a valid answer.")
		continue
