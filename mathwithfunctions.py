def add(a, b):
    print("Adding", a, b)
    return a + b

def subtract(a, b):
    print("Subtracting", a, b)
    return a - b

def multiply(a, b):
    print("Multiplying", a, b)
    return a * b

def divide(a, b):
    print("Dividing", a, b)
    return a / b

print ("Only with Functions !")

age = add(23, 10)
height = subtract(12, 2)
weight = multiply(23, 7)
iq = divide (34 , 3)

print("Age: Height: Weight:, IQ:", age, height, weight, iq)

print("Here is the puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print ("That will be ", what ) 
