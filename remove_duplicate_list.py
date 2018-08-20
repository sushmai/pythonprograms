#funcrion that takes a list and returns new list with out duplicates

def removeduplicate(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return(b)

#using set
def duplicate(c):
    return(list(set(c)))

a = [1,2,3,1,23,1]
c = [1,1,1,1,12,2,2,2,3,3,3,4,4,4,5,5,5]
print(a)
print(removeduplicate(a))
print(c)
print(duplicate(c))
    
