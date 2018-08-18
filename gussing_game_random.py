import random
a = random.randint(1,9)
guess = int(input("please enter a number between 1 t0 9 : "))
print("rangom number is", a)
if guess == a :
    print("your guess is correct")
elif (guess < a ):
    print("the number is larger than you guessed")
else:
    print("the number is smaller than you guessed.")
