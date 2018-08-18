#program to combine to lists with out duplicate.

a = [1,2,3,4,5]
b = [5,4,5,6,7,1]
print(set(a) & set(b))
for a in b:
    print(a)
