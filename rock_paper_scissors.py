import time
from random import choice

SHAPES = ['rock', 'paper', 'scissors']
CHOICE_PROMPT = "\nWhat are you going with? "
CHOICE_PROMPT += SHAPES[0].title() + ", " + SHAPES[1].title() + " or "
CHOICE_PROMPT += SHAPES[2].title() + "? "


def rock_paper_scissors_callout():
    """Print the 'players' calling out the name of the
    'shapes'."""
    print("\nHere we go...\n\nRock!")
    time.sleep(1)
    print("\nPaper!")
    time.sleep(1)
    print("\nScisssors!")
    time.sleep(1)
    print(f"\nComputer chose... {computer_choice.title()}!")
    time.sleep(1)


def win_scenarios():
    """Check to see if user or computer wins game."""
    if user_choice_input == 'rock' and computer_choice == 'paper':
        print("\nPaper covers Rock... you lose!\n")
    elif user_choice_input == 'paper' and computer_choice == 'rock':
        print("\nPaper covers Rock... you win!\n")
    elif user_choice_input == 'rock' and computer_choice == 'scissors':
        print("\nRock crushes Scissors... you win!\n")
    elif user_choice_input == 'scissors' and computer_choice == 'rock':
        print("\nRock crushes Scissors... you lose!!\n")
    elif user_choice_input == 'paper' and computer_choice == 'scissors':
        print("\nScissors cuts Paper... you lose!\n")
    elif user_choice_input == 'scissors' and computer_choice == 'paper':
        print("\nScissors cuts Paper... you win!\n")


while True:
    computer_choice = choice(SHAPES)
    new_game = input("Do you want to play Rock Paper Scissors? (yes/no) ")
    new_game = new_game.lower()
    new_game = new_game.strip()
    if new_game in ('y', 'yes'):
        user_choice_input = input(CHOICE_PROMPT)
        user_choice_input = user_choice_input.lower()
        user_choice_input = user_choice_input.strip()
        if user_choice_input not in SHAPES:
            print("That is not a valid entry!")
            continue
        elif computer_choice == user_choice_input:
            rock_paper_scissors_callout()
            print(f"\nTie! You both chose {user_choice_input.title()}!\n")
            continue
        else:
            rock_paper_scissors_callout()
            win_scenarios()
            continue
    elif new_game in ('n', 'no', 'q', 'quit'):
        break
    else:
        print("That is not a valid answer.")
        continue
