# Arrtibutes
# what methods needed to interact with Variables / Arributes

#wardrode
"""
Cothing : Class

# Attributes / instance variables
Name :
clean

# Methods we need

.getName()
.isClean()

"""
class Clothing(object):
    def __init__(self, name, clean = True):
        self.name = name
        self.clean = clean

    def getName(self):
        return self.name

    def isClean(self):
        return self.clean
    def __str__(self):
        return "Clothing[name= " + self.name + \
               ",clean = " + str(self.clean) + \
               "]"
        
def main():
    #test the clothing class
    myJeans = Clothing("Blue Jeans", False)
    myShirt = Clothing("WhiteShirt")
    print(myJeans.getName())
    print(myShirt.isClean())
    print(myJeans)
  



if __name__ == "__main__":
    main()
