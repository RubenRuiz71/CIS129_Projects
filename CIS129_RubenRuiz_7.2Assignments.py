# Lab 7-3 The Dice Game
# This program simulates a dice game where two players roll dice and the player with the higher roll wins.

import random

# the main function
def main():
    # initialize variables
    end_program = 'no'
    player_one = 'NO NAME'
    player_two = 'NO NAME'

    # while loop to run program again
    while end_program == 'no':
        # populate variables
        player_one, player_two = input_names(player_one, player_two)

        # initialize variables for the dice rolls and winner name
        winner_name = 'NO NAME'
        p1_number = 0
        p2_number = 0

        # call to rollDice
        winner_name = roll_dice(p1_number, p2_number, player_one, player_two)

        # call to displayInfo
        display_info(winner_name)

        # prompt to end program
        end_program = input('Do you want to end the program? (yes/no): ')

# this function gets the players' names
def input_names(player_one, player_two):
    player_one = input('Enter the name for Player 1: ')
    player_two = input('Enter the name for Player 2: ')
    return player_one, player_two

# this function will get the random values for dice rolls and determine the winner
def roll_dice(p1_number, p2_number, player_one, player_two):
    # generate random dice rolls
    p1_number = random.randint(1, 6)
    p2_number = random.randint(1, 6)

    # determine the winner
    if p1_number > p2_number:
        winner_name = player_one
    elif p2_number > p1_number:
        winner_name = player_two
    else:
        winner_name = 'TIE'

    return winner_name

# this function displays the winner
def display_info(winner_name):
    print(f'The winner is: {winner_name}')

# calls main
if __name__ == "__main__":
    main()
