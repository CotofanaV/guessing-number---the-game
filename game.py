

import random
import time

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


decizie = input("Do you want to play? Choose y / n: ")
while True:

    if decizie == "y":
        print("Let's get started!")
        play()

    elif decizie == "n":
        print("Maybe another time!")
        quit()


    else:
        print("Choose y sau n")
        decizie = input()
