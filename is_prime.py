number = int(input("enter a number "))
mylist = [i for i in range(2, number-1) if number % i == 0]
def is_prime(number):
    if len(mylist) == 0:
        print(number, "is prime" )
    else :
        print(number, "is not prime and is divisible by : ")
        print(mylist)
is_prime(number)
