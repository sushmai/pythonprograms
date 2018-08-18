# printing only comman elements
a = [1,2,4,5,6,7,8,9,98,43,2]
b = [8,2,3,1,2,43,54,67,7,76,45,343,223]

result = [i for i in a if i in b ]
print(result)

# with random
import random
x = random.sample(range(1,10), 4)
print(x)
y = random.sample(range(1,10), 5)
print(y)
result = [i for i in x if i in y]
print(result)

# with out repeating
c = [1,2,3,4,5,6,7,8,9,10,2,2,2]
d = [1,2,4,3,5,6,7,8,9,10,11,2,12,23,12,6]

result_overlap = [i for i in set(c) if i in d ]
result = []
for element in result_overlap:
    if element not in result:
        result.append(element)
print("result is", result)

# using random - with out repeating
e = random.sample(range(1,10), 6)
f = random.sample(range(1,15), 8)
print("e is :",e)
print("f is :",f)
results = [i for i in set(e) if i in f]
result = [i for i in results if results.count(i) == 1]
print("result without overlap", result)
