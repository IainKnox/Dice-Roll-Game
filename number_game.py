"""
Number Game is a program that rolls a pair of dice
and asks the user to guess hte sum thereof. If the
user is right, the win! Otherwise the computer wins.
"""
from random import randint
# randint is used to generate random numbers
# within a preset dice size


from time import sleep
# used to create pauses between rolls


def get_user_guess():
    """ ask the user to guess the total sum"""

    guess = int(input("Enter your guess: "))
    return guess


def roll_dice(number_of_sides):
    """ generate dice rolls with a max value based
    on the number of sides the dice has"""

    first_dice = randint(1, number_of_sides)
    second_dice = randint(2, number_of_sides)
    max_val = number_of_sides * 2
    print(f"The highest guess possible is {max_val}")
    guess = get_user_guess()
    if guess > max_val:
        print("That is an invalid number")
    else:
        print("Rolling...")
        sleep(2)
        print(f"The first dice rolled a {first_dice}")
        sleep(1)
        print(f"The second dice rolled a {second_dice}")
        sleep(1)
        total_roll = first_dice + second_dice
        print(total_roll)
        print("Result...")
        sleep(1)
        if total_roll == guess:
            print("Whoop Whoop, you won!!")
        else:
            print("Oh no, you lost!!")


roll_dice(6)
