### GUESSING GAME - PROGRAM SELECTS A RANDOM NUMBER BETWEEN TWO NUMBERS AND PLAYER GUESSES THE CORRECT ONE ###

import math #imports the math library
import random # imports the random library
a = [] #list of variables
a.append(random.randint(1, 99)) # this adds the var and returns the var from specific range
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
a.append(random.randint(1, 99))
for i in range(10)::# loop for generating a sequence of numbers
    g = int(input("Enter an integer from 1 to 99: ")) # asks for int in g
    while a[i] != g: #condition when int is different from g
        if g < a[i]: #condition if g is smaller from a
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))# asks for int in g
        elif g > a[i]: #condition if the previous statement isnt true but checks for another
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: ")) # asks for int in g
        else: #checks if statement if is false
            break #break is with upper condition 
    print("you guessed it!") # prints the information

b = [] # list of vars
b.append(random.randint(1, 49)) # this adds the var and returns the var from specific range
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):# loop for generating a sequence of numbers
    g = int(input("Enter an integer from 1 to 49: ")) #asks for an integer
    while b[i] != g: #condition while b int is different from g int
        if g < b[i]: #condition if g int is smaller than b int
            print("guess is low") #printed message
            g = int(input("Enter an integer from 1 to 49: "))#asks for g int again
        elif g > b[i]: #condition if the previous statement isnt true but checks for another
            print("guess is high")#printed message
            g = int(input("Enter an integer from 1 to 49: "))# asks for int in g
        else:# checks if statement if is false
            break #then breaks with upper condition
    print("you guessed it!") # prints message