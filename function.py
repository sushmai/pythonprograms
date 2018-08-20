"""
# defining function
def my_function():
    # add whatever needed
    print("Hello from function")

#call the function
my_function() #this will go back and exeucte code with in function

def my_country(country = "USA"):
    print("I am from " + country)
my_country("INDIA")
my_country("Japan")
my_country("UK")
my_country()
"""
"""

def greet(name):
    print("Hello," + name + ".... Good morning!!")
greet('sam')

def my_func():
    x = 10
    print("Value inside function:", x)

x = 20
my_func()
print("Value outside function:", x)




import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
 
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, errors )

def multiplication(x):
    return x * 5

print(multiplication(5))
print(multiplication(23))
print(multiplication(22))

def print_a():
    print("Helo world")
    print("welcome to python")

def main():
    print_a()

main()
"""
def add(a,b):
    return(a+b)
c = add(3,4)
print(c)






























    
