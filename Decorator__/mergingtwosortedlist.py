#method 1
a = [3,4,5,7,2,4]
b = [34,5,3,4444]

c = []
# a or b should not be empty
while a and b :
    if a[0] < b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))
print(c+a+b)

#method 2
a = [3,4,6,10,11,18]
b = [1,5,7,12,13,19,21]
c = [23,4,12,54,6,44]

a.extend(b)
print(a)
a.extend(c)
print(a)
a = sorted(a)
print(a)
