# create class
class Dog:
    
    #class attributes
    species = "mammal"

    #instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def description(self):
        return("{} is {} years old".format(self.name, self.age))
    def speak(self, sound):
        return("{} is {}".format(self.name, sound))

#inherit the class
class RussellTerrier(Dog):
    def run(self, speed):
        return("{} runs {} mph".format(self.name, speed))

class Bulldog(Dog):
    def run(self, speed):
        return("{} runs {}".format(self.name, speed))
    
#child classes inherit attributs and behaviour from parent class
jim = Bulldog("jim", 12)
print(jim.description())

#child classes have specific attributes and behaviours
print(jim.run("Slowly"))
    
        








"""
# create a class
class Dog:
    # classattributes
    species = "Mammal"

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # instance methods used to handle 
    def description(self):
        return("{} is {} years old".format(self.name, self.age))
    
    # instance method
    def speak(self, sound):
        return("{} says {}".format(self.name, self.speak))

# instantiate the class object
philo = Dog("Philo", 6)

# call instance methods
print(philo.description())
print(philo.speak("Gruff "))
    


# creating Dog class
class Dog:

    #class Attributes
    spices = "mammal"
    
    # Instance attributes    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Initialize class objects 
philo = Dog("philo", 4)
rockey = Dog("Rockey", 5)
mikey = Dog("Mikey", 7)

# Access the attributes
def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {}".format(get_biggest_number(philo.age, rockey.age,mikey.age)))

"""


    
        
