# print
print("Hello, World!")

#if-else
"""
n is odd print weird
n is even and inclusive of 2 and 5 print not weird
n is even and inclusive of 6 to 20 print weird
n is even greater that 20 print not weird
"""
print("please enter a number...")
n = int(input())

if (n % 2 != 0 ) or (n % 2 == 1 and 6 <= n <= 20):
    print("Weird")
elif (n % 2 == 0) and (2 <= n <= 5 or n > 20):
    print("Not weird")
# Airthmetic Operations :
"""
Read two integers from STDIN and print three lines
1.Sum of two numbers
2. Difference of two numbers
3. product of two numbers:
"""

print("enter 'a' value ")
a = int(input())
print("enter 'b' value")
b = int(input())
print("a + b =  ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a % b = ", a % b)
print("a // b = ", a // b )
print("a / b = ", a / b)

# loops
# for i in range of n print i pow 2 
print("Enter 'n' value :")
n = int(input())
for n in range(0,n):
    print(n ** 2)
# Writing Function :
"""
leap year
The year can be evenly divided by 4 is leap year Unless:
    the year can evenly divided by 100 is not a leap year, unless
        the year also can evenly divisible by 400 the leap year
"""
print("Enter 'year'")
def is_leap(year):    
    leap = False
    if (year % 4 == 0) or (year % 100 != 0 and year % 400 == 0):
        return True
    else:
        return leap

year = int(input())
print(is_leap(year))

"""
read an inter N
with out string method, print following
123.. n (upto  n )
"""
print("enter value for i ")
i = int(input())
print(*range(1,i+1), sep = "")
