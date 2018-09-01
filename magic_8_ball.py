# Using list :
#
import random
def main():
    print("Magic 8 ball predicts the future:")

    replies = ["Yes !",
               "Signs POints to Yes!",
               "I don't think so",
               "Reply Hazy, try later",
               "No !!"
               ]
    

    # Have the user enter a question :
    question = input("Enter a yes or no question : ")


    # Reply to the question with random Yes or no or maybe answer
    rand_value = int(random.random() * 4) # "*4" means 0 to 3 inclusive
    print(replies[rand_value])

   

if __name__ == "__main__":
    main()

