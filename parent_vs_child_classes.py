# create  a class

class Dog:
    #class attributes
    species = "mammal"

    #instace attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instace method
    def description(self):
        return("{} is {} old".format(self.name, self.age))
    #instace method
    def sound(speak):
        return("{} is {}".format(self.name, speak))


# child class - Inherit the parent class
class RussellTerrier(Dog):
    def run(self, speed):
        return("{} runs {}".format(self.name, speed))

# child class - Inherit from parent class
class Bulldog(Dog):
    species = "reptile"
    def run(self, speed):
        return("{} runs {}".format(self.name, speed))

#child classes inherit attibutes and behaviors from the parent class

jim = Bulldog("Jim", 12)
print(jim.description())

# child class have specif attributes and behaviors as well

print(jim.run("slowly"))

# is jim an instance of parent(DOG()) class ?
print(isinstance(jim, Dog))

# is philo is an instance of DOG class ?
philo = Dog("philo", 10)
print(isinstance(philo, Dog))

# instance of child class
rocky = RussellTerrier("rocky", 3)
print(isinstance(rocky, Bulldog))

#print(isinstance(philo, jim))

"""
we can ovverride the functionality of parent class

"""
frank = Dog()
print(frank.species)

beans = Bulldog()
print(beans.species)















    
