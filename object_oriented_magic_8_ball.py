# Using list :
#
import random

# setup a class 
class Magic_8_ball:
    """ Magic_8_ ball class defines magic_8_ball_objects:
    3 basic kinds
    1 - how object constructed 
    """
    # 1 - how object constructed
    # self referes to object itself 
    def __init__(self):
        # give the details that magic_8 ball needs to know about itself

        self.replies = ["Yes !","Signs POints to Yes!","I don't think so","Reply Hazy, try later","No !!","Definitetly Not"]
        # 2 - class needs to allow interactions with itself
        # using methods(mutated method)

        self.reply = ""
        self.shake()

    def shake(self):
        """
            The shake method mutates the magic_8_ball object
            to set a new random reply
            """
        rand_value = int(random.random() * len(self.replies))
        self.reply = self.replies[rand_value]
    def get_reply(self):
        return(self.reply)
        
        


def main():
    print("Magic 8 ball predicts the future:")
    my_8_ball = Magic_8_ball()    

    while True: 
        # Have the user enter a question :
        question = input("Enter a yes or no question : ")

        my_8_ball.shake()
        print(my_8_ball.get_reply())
        
        
        #Ask if they want's to try again
        go_again = input("Would you like to ask another question ??")

        if go_again[0].lower() == "n":
            break
        
    print("Good Bye ")

       

if __name__ == "__main__":
    main()

