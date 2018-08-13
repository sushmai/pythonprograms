def add(a, b):
    print("Adding : ", {a} + {b})
    return a + b

def subtract(a, b):
    print("Subtracting:",{a} - {b} )
    return a - b

def multiply(a, b):
    print("Multiplying : ", {a} * {b})
    return a * b

def divide(a, b):
    print("Dividing:", {a} / {b})
    return a / b

print ("Implementing math with functions ! ")

age = add(34, 23)
height = subtract(56, 4)
weight = multiply(54, 54)
iq = divide(34,23)

print("Age:", {age},"Height:",{Height}, "Weight:", {weight} , "iq", {iq})

print("Calculations : ")

what = add(age, subtract(height,multiply(weight, divide(iq,2)))))

print("That is ", what)
