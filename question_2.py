"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""

def factorial(n):
    result = 1
    i = n * (n-1)
    while n >= 1:
        result = result * n
        n = n - 1
    return result
print(factorial(5))
# with out function
n = int(input("please enter a number:"))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("the factorial of", n ," is : ", end="")
print(fact)
# using import math
import math
n = int(input("please enter a number : "))
print(math.factorial(n))
