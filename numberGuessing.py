#Number Guessing Game

import random

random.seed(None, 2)

number = random.randint(1, 9)
chances = 5
print("I have a number that is an integer with a value anywhere from 1 to 9. Guess my number!")
guess = int(input("Type your guess: "))

while chances > 0:
    if guess > number:
        print("Your guess was too high!")
        chances = chances - 1
    elif guess < number:
        print("Your guess was too low!")
        chances = chances - 1
    else:
        print("Amazing! You guessed correctly!")
        print("You won the game.")
        break

    if chances == 0:
        print("Unfortunately, you have run out of chances.")
        print("Here was the number:", number)
        print("You lost the game. Better luck next time!")
        break
    else:
        guess = int(input("Type your guess: "))