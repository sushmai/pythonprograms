#!/usr/bin/env python
import random

def main():
    randomNumber = random.randint(1,100)
    found = False
    
    while not found:
        guess_number = int(input("Guess a number between 1 to 100 : "))

        if guess_number == randomNumber:
            print("Sucess, you got it right!!")
            found = True
            
        elif guess_number < randomNumber:
            print("Guess Higher number")
            
        else:
            print("Guess lower number")

            
    print("Thanks for playing ")



if __name__ == "__main__":
    main()
