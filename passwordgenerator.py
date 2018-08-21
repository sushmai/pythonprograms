import random
import string
password = []
#a = []
#a = str(input("do you want 'strong' or 'weak' password ? "))

def generate(password):
    #a = []
    a = str(input("do you want 'strong' or 'weak' password ? "))
    #password = []

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    number = string.digits
    everything = upper + lower + special + number

    while len(password) != (6 or 12):
        if a == "strong" :
            password = random.sample(everything, 12)
            return("".join(password))

        elif a == "weak":
        
            password = random.sample(everything, 6)
            return("".join(password))
        else:
            a = str(input("select again "))
            #print(f"Please select only from..'strong' or 'weak'")
            #return
print((generate(password)))
#print(a)
#else case is not working
