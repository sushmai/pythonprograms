"""
Rules :
    Rock beats scissors
    scissors beats paper
    paper beats rock

"""
import sys
user1 = input("enter your name:")
user2 = input("enter your name:")

user1_answer = input("%s, do you want rock, scissors or paer ?" %  user1)
user2_answer = input("%s, do you want rock, scissorrs or paper?" % user2)

def compare(u1,u2):
    if u1 == u2 :
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("rock wins !")
        else:
            return("paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("scissors wins!")
        else:
            return("rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("paper wins!")
        else:
            return("scissors wins!")
    else:
        return("Invalid input !! please select from rock, scissors, paper")
        sys.exit()

print(compare(user1_answer, user2_answer))
    
