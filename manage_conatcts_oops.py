#!/usr/bin/env python3 #shebang line

"""
This program allows to manage my contacts
"""

class Person(object):
    """
The person class defines a  person in terms of Name, phone number, email
we need three things 
"""
    #1. Constructor
    # How you take information from main
    # self referes object itself - the instance of object
    # special costructor method __init__
    
    def __init__(self, theName, thePhone, theEmail):
        self.name = theName # saves for only for this perticulat object
        self.phone = thePhone
        self.email = theEmail    

    # Accesser Methods(getter)
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email
    

    #Mutator Methods(setters)
    def setPhone(self, newPhone):
        self.phone = newphone
    def setEmail(self, newEmail):
        self.email = newEmail

    # to get the data instead of memory location so need to override
    def __str__(self):
        return ("Person[name=" + self.name + \
                ",phone=" + self.phone + \
                ",email=" + self.email + \
                "]")
      
def main():

    friend1 = Person("Jill", "333", "jill@gmail.com")
    print(friend1.getEmail())
    friend1.setEmail("Jill1@email.com")
    print(friend1.getEmail())
    print(friend1)


if __name__ == "__main__":
    main()
    
