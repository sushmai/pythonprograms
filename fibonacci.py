# next number is sum of previous two numbers (1,1,2,3,5,8,13,21..... n )
"""
a = int(input("Enter a number :"))
if a == 1:
    b = [1]
elif a != 1:
    b = [1,1]
    for i in b:
        if len(b) < a:
            i = b[-1] + b[-2]
            b.append(i)
print(b)

# using function :
def Fibonacci(num):
    a = 0
    b = 1
    if num == 1:
        print(0)
        return
    elif num == 2:
        print(a, b)
        return
    elif num > 2:
        count = 2
        print(b)
        while count <= num:
            c = a + b
            a = b
            b = c
            print(c)
            count += 1
    else:
        print("invalid")
num = int(input("enter the number:"))
Fibonacci(num)

# using function 
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range(1,11):
    # each time it will call the all values (calcultes again and againg memory and performance issue)
    print(n, ':', fibonacci(n))

# using memoization :
# 1. Implement explicitely to see how it works :
# dictionary to srote recent function calls (fibonacci values)
fibonacci_cache = {}
def fibonacci(n):
    #if we have cached the value then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2 :
        value = fibonacci(n-1) + fibonacci(n-2)
    #cache the value and return it
    fibonacci_cache[n] = value
    return value
for n in range(1,30):
    print(n, ':', fibonacci(n))
"""
# 2. Built in python tool that makes momoization trivial
from functools import lru_cache
@lru_cache(maxsize = 1000)# default 1028 values
def fibonacci(n):
    # doesn't work for float or -ve points or string
    # so give user feedback
    #check that the input is positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise TypeError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

"""
# doesn't work for float or -ve points or string 
for n in range(1, 34):
    print(n, ":", fibonacci(n))
    
"""   











    
    
