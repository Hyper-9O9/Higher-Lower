import os
from art import logo,vs
from HL_Data import  data
from random import choice

def compare(option_A, option_B, player_choice):
    '''Return True value if the choice is correct'''
    if player_choice == 'A':
        if option_A['follower_count'] > option_B['follower_count']:
            return True
        else:
            return False

    elif player_choice == 'B':
        if option_B['follower_count'] > option_A['follower_count']:
            return True
        else:
            return False


in_game = False
player_score = 0

option_A = choice(data)

while not in_game:
    # initializing the variables to compare
    option_B = choice(data)

    # checking if the two options are not the same
    if option_A == option_B:
        same_option = False
        while not same_option:
            option_B = choice(data)
            if option_A is not option_B:
                same_option = True

    # if the player has no score just show the options
    if player_score == 0:
        # printing logo and options
        print(logo)
        print(f"Compare A: {option_A['name']}, is a {option_A['description']}, from {option_A['country']}")
        print(vs)
        print(f"Against B: {option_B['name']}, is a {option_B['description']}, from {option_B['country']}")
    # if the player scored, show his/her score
    else:
        # printing logo, options, and score
        print(logo)
        print(f"You're right! Current Score: {player_score}.")
        print(f"Compare A: {option_A['name']}, is a {option_A['description']}, from {option_A['country']}")
        print(vs)
        print(f"Against B: {option_B['name']}, is a {option_B['description']}, from {option_B['country']}")

    # getting answer of the player
    player_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    # comparing the answer
    # if true increase score and keep on playing
    if compare(option_A= option_A, option_B= option_B, player_choice= player_input) is True:
        os.system('cls')
        option_A = option_B
        player_score += 1
    # if false end game
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's incorrect. Final score: {player_score}")
        in_game = True

# making the screen wait till the user presses enter
input()
