def print_max(x,y):
    ''' prints the maximum of two numbers.
        the two values must be integers.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")
print_max(3,4)
print(print_max.__doc__)


"""
def total(a = 5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,2,2,2, jack= 232323, john = 656565, jon = 56565 ))




def func(a = 3, b = 5, c = 12):
    print('a is',a, 'b is', b, 'c is', c)


func(a = 4, c = 87)
func(a = 45, b = 67, c = 98)
func()


def say(message, times = 1):
    print(message * times)

say('Hello')
say("one", 5)



def say_hello(): # defining the function
    #block belonging to the function
    print("Hello WOrld")
# end of the function   
say_hello()# call the function any where and as many times as you want 
say_hello()

def print_max(a,b):
    if a > b :
        print("maximun number is: ", a)
    elif a == b:
        print(a, "is equal to ", b)
    else:
        print(b," is maximum")

#pass the values to the function

print_max(5,8)

x = 4
y = 3

# pass variables as arguments
print_max(x,y)

# local Variable :

x = 50
def func(x):
    print ("x is ", x)
    x = 2
    print ("changes to local x" , x)
func(x)
print("x is still", x)

x = 34
def func():
    global x
    print("x is ", x)
    x = 6
    print("changes in x value", x)

func()
print("Value changed globally ", x)
"""

