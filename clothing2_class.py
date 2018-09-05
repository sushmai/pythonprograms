# Inheritance
#Arrtibutes
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
    def __init__(self, name, clean = True, times_worn=0, max_wears=1):
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears

    def getName(self):
        return self.name

    def isClean(self):
        return self.clean    
    
    def wear(self):
        self.times_worn += 1
        if self.times_worn >= self.max_wears:
            self.clean = False
            
    def wash(self):
        self.clean = True
        self.times_worn = 0
        
    def __str__(self):
        return "Clothing[name= " + self.name + \
               ",clean = " + str(self.clean) + \
               ",times_worn = " + str(self.times_worn) + \
               ", max_wears = " + str(self.max_wears) + \
               "]"
# Inheritance 
class Shirt(Clothing):
    def __init__(self, name, clean = True, times_worn = 0, max_wears = 1, short_sleeves = True):
        super().__init__(name, clean, times_worn, max_wears)
        self.short_sleeves = short_sleeves
    def hasShortSleeves(self):
        return self.short_sleeves
    def __str__(self):
        return "Shirt[" + super().__str__() + \
               ",ShortSleeves = " +str(self.short_sleeves) + \
               "]"


def main():
    #test the clothing class
    """
    myJeans = Clothing("Blue Jeans", False)
    myJeans.wear()
    print(myJeans)
    myJeans.wash()
    print(myJeans)
    myShirt = Clothing("WhiteShirt")
    print(myJeans.getName())
    print(myShirt.isClean())
    print(myJeans)
    """
    myClothes = []
    myClothes.append(Clothing("blue jeans", False))
    myClothes.append(Clothing("cap", True, 20, 1000))
    myClothes.append(Clothing("Jacket", True, 10, 200))
    myClothes.append(Shirt('T-Shirt', True, 0, 1, True))
    myClothes.append(Shirt("Dress", True, 0, 1, False))

    print("\n ====== Full Wardreobe =======")
    for i in range(len(myClothes)):
                   print(myClothes[i])
    print("\n******** Clean Clothes********")
    for i in range(len(myClothes)):
        if myClothes[i].isClean():
            print(myClothes[i])
    print("\n**********Dirty Clothes*********")
    for i in range(len(myClothes)):
        if not myClothes[i].isClean():
            print(myClothes[i])
    print("\n******* shirts*******")
    myClothes[4].wear()
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            if myClothes[i].isClean():
                print(myClothes[i])
if __name__ == "__main__":
    main()
