### GUESSING GAME - PROGRAM SELECTS A RANDOM NUMBER BETWEEN TWO NUMBERS AND PLAYER GUESSES THE CORRECT ONE ###

import math 
import random 

nr = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99:"))
while nr != guess:
    if guess < nr:
        print("guess is too low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > nr:
        print("guess is too high")
        guess =  int(input("Enter an integer from 1 to 99: "))
    else: break
