n = int(input("Enter an integer: "))
reverse = 0
while (n>0):
    reminder = n%10
    reverse = (reverse * 10)+reminder
    n = n//10
print(reverse)
