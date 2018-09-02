#!/usr/bin/env python3 #shebang line

"""
This program allows to manage my contacts
"""

def main():

    friends = []
    for i in range(2):    
        print("contact manager")
        name = input('enter name:')
        phone = int(input("enter phone:"))
        email = input("Enter email : ")
        friends.append([name,phone,email])

    for i in range(len(friends)):
        print("contact info ")
        for j in range(len(friends[i])):
            print(friends[i][j])


if __name__ == "__main__":
    main()
    
