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
