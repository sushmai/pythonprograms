
i = 0
numbers = []

while i < 6 :
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1

    print("Numbers now:", numbers)
    print(f"at the bottom i is {i}")

print("The numbers:")

for num in numbers:
    print(num)
"""
#while loop for truth tables: infinite loop ctrl + c to end
while True:
    age = int(input('enter your age:'))
    if (age > 12 and age < 18):
        print("Sorry you are not allowed to watch.")
    elif age <= 12:
        print("You can watch comic")
    else:
        print("You can watch as you wish")

"""
