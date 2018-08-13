def binarysearch(ls, data):
    first = 0
    last = len(ls)-1
    done = False

    while first <= last and not done:
        mid = (first+last)//2
        if ls[mid] == data:
            done = True

        else :
            if ls[mid] > data :
                last = last - 1
            else:
                first = first + 1
        return done

print(binarysearch([2,5,6,3,78,23,1],4))






"""
import random

anum = 9
size = 10
array = random.sample(list(range(1,20)), size)
array = sorted(array)

print(anum, array)

def binary_search(number, array, lo, hi):

    if hi < lo: return -1
    mid = (lo + hi) // 2
    if number == array[mid]:
        return mid
    elif number < array[mid]:
        return binary_search(number, array, lo, mid -1 )
    else:
        return binary_search(number, array, mid + 1, hi)

def my_search(anum, array):
    return binary_search(anum, array, 0, len(array) - 1)
pos = my_search(anum, array)

if pos < 0 :
    print("not found")
else:
    print("found at position", pos)

"""
