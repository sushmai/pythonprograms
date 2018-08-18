# 1.number is multiple of 4 print different message
# 2. divide  a with b and check results. 
a = int(input("enter a number: "))
b = int(input("enter another number:"))
if (a % 4 == 0 ):
    print ( a," is multiple of 4")
elif(a % b == 0 ):
    print(a,"is divisible by", b)
else:
    print(a ,"is neither multiple of 4 nor divisible by ", b)

#Method 1 
num = int(input("Enter a number :"))
mod = num % 2
if mod > 0 :
    print("The number is odd number.")
else:
    print("The number is even number. ")



#Method 2
#for single input easy way 
n = input("enter a number : ")
if (int(n) % 2 == 0):
    print("Even")
else:
    print("odd")


