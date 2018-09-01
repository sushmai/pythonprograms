# Using list :
#
import random
def main():
    print("Magic 8 ball predicts the future:")

    replies = ["Yes !",
               "Signs POints to Yes!",
               "I don't think so",
               "Reply Hazy, try later",
               "No !!",
               "Definitetly Not"
               ]

    while True: 
        # Have the user enter a question :
        question = input("Enter a yes or no question : ")


        # Reply to the question with random Yes or no or maybe answer
        # what if we want to add more replies in futute, so instead of changing the
        # number after "*" we can assign it to len of the list 
        rand_value = int(random.random() * len(replies)) 
        print(replies[rand_value])
        #Ask if they want's to try again
        go_again = input("Would you like to ask another question ??")

        if go_again[0].lower() == "n":
            break
    print("Good Bye ")

       

if __name__ == "__main__":
    main()

