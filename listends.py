import random
import randint
def random_list():
    list_a = list(random.sample(range(100),random.randint(0,12)))
    print("Random list is {}".format(list_a))
    return(list_a)

def first_and_last(list_a):
    new_list = [list_a[0],list_a[-1]]
    return(new_list)

x = first_and_last(random_list())
print(x)
