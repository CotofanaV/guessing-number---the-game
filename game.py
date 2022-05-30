

import random
import time
from tkinter import Y

def choose_interval():
    print("Choose a range of numbers in which you want to play.")
    time.sleep(2)
    n1 = int(input("First number: "))
    n2 = int(input("Second number: "))
    if int(n1) <= int(n2):
        a = n1  
        b = n2
        return(a,b)    
    else:
        a = n2
        b = n1
        return(a,b)



def play():
    
    a,b = choose_interval()
    guess_number = random.randint(a,b)
    number = int(input("Select a number between " + str(a) + " and " + str(b) +"\n"))
    guessing_count = 1
    print("You tried: ", guessing_count)
    while True:

        if number != guess_number and number <= guess_number:
            print("Choose a number greater than ",number)            
            number = int(input())
        elif number != guess_number and number >= guess_number:
            print("Choose a number smaller than ",number)           
            number = int(input())

        else:
            print("You guessed it!!")
            quit()
        guessing_count += 1
        print("You tried: ", guessing_count)

decision = input("Do you want to play? Choose y / n: ")
while True:

    if decision == "y":
        print("Let's get started!")
        play()

    elif decision == "n":
        print("Maybe another time!")
        quit()


    else:
        print("Choose y sau n")
        decision = input()
