#
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)
    # complete this line with a reduce statement
    return t.numerator, t.denominator
# multiply all numbers in a list :
data = [1,2,3,4,5,6,7,8,9,10]

multiplier = lambda x, y : x * y
print(reduce(multiplier, data))
# instead reduce use for
product = 1
for x in data:
    product = product * x

print("product is", product)
