num = int(input("enter a number"))
listrange = list(range(1, num+1))
divisorList = []

for number in listrange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
        
a = int(input("enter a number:"))
c = list(range(1, a+1))
b = []

for i in c:
    if a % i == 0:
        b.append(i)

print(b)
