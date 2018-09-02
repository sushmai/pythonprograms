#!/usr/bin/env python3

# to keep track og contacts and take input from user

class Person(object):
    #constuctor
    def __init__(self, theName, thePhone, theEmail):
        self.name = theName
        self.phone = thePhone
        self.email = theEmail

    # Accesser Methods(getters)
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email

    # Mutator Methods(setters)

    def setPhone(self, newPhoneNumber):
        self.phone = newPhoneNumber
    def setEmail(self, newEmailAddress):
        self.email = newEmailAddress
    def __str__(self):
        return("Person[name=" + self.name + \
               ",phone=" + self.phone + \
               ",email=" + self.email +\
               "]")
def enter_a_friend():
    name = input("Enter friend's name:")
    phone = input("enter a phone number:")
    email = input("Enter email Address:")
    return Person(name, phone, email)

def lookup_a_friend(freinds):
    found = False
    name = input("Enter a name to lookup:")
    for freind in freinds:
        if name in freind.getName():
            print(freind)
            found = True
        if not found:
            print("Name does not match with exisitng contacts")

def show_all_friends(friends):
    print("Show  all contacts:")
    for friend in friends:
        print(friend)


def main():
    friends = []
    running = True
    while running:
        print("\nContacts Mangaer")
        print("1) new contact 2)lookup")
        print("3) show all    4) End")
        option = input(">")
        if option == "1":
            friends.append(enter_a_friend())
        elif option == "2":
            lookup_a_friend(friends)
        elif option == "3":
            show_all_friends(friends)
        elif option == "4":
            running = False
        else:
            print("Unrecognized input, Please try again.")
    print("Program Ending")

if __name__ == "__main__":
    main()

        




























            


































