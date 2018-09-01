import random
def main():
    print("Magic 8 ball predicts the future:")

    # Have the user enter a question :
    question = input("Enter a yes or no question : ")


    # Reply to the question with random Yes or no or maybe answer
    rand_value = int(random.random() * 4) # "*4" means 0 to 3 inclusive

    if rand_value == 0:
        print("Yes !")
    elif rand_value == 1:
        print("Signs point to yes !!")
    elif rand_value == 2:
        print("Reply hazy..., ask again later ")
    else:
        print("I don't think so!")


if __name__ == "__main__":
    main()
    
# what if we want to give 20 random messages the will be 20 if else cases instead we can
#  use data strusctures (list in this case. )
