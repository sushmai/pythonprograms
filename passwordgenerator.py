import random
import string
password = []
a = []
def generate(password):
    a = str(input("do you want 'strong' or 'weak' password ? "))
    password = []

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    number = string.digits
    everything = upper + lower + special + number

    if a == "strong" :
        password = random.sample(everything, 12)
        return("".join(password))
    elif a == "weak":
        password = random.sample(everything, 6)
        return("".join(password))
    else:
        print(a)
    return
print((generate(password)))
# print(a)
#else case is not working
