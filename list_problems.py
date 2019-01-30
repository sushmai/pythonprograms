
# to get larger number from list
def large_num(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(large_num([2,3,5,2,45]))

def largest_number(list):
    list.sort()
    return list[-1]
print(largest_number([1,2,4,5,2,3,4]))

list1 = [1,2,3,4,5,6,7,8]
print(max(list1))


def sum_of_numbers(list1):
    return(sum(i for i in list1))
print(sum_of_numbers([1,2,3,4,5]))
    
def mul_of_nums(list):
    mul = 1
    for i in list:
        mul  *= i
    return mul
print(mul_of_nums([1,2,3]))


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


def sum_of_list(list1):
    sum_of_num = 0
    for i in list1:
        sum_of_num += i
    return(sum_of_num)
print(sum_of_list([1,2,3,4,5]))

# to get smallest number in list
def smallest(list):
    min = list[0]
    for i in list:
        if i  < min:
            min = i
    return min
print(smallest([1,2,3,4,5]))
        
list1 = [-1,-2,-3]
print(min(list1))

list2 = [4,2,5,2,5,1,-3]
list2.sort()
print(list2[0])

def str_length(list):
    count = 0

    for word in list:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
    return count     

print(str_length(['abc', 'xyz', 'aba', '1221', '11']))

"""
# remove duplicates from list
"""
def remove_duplicates(list1):
    s = []
    for i in list1:
        if i not in s:
            s.append(i)
    return s

print(remove_duplicates([1,1,1,2,3,4,5,3,2,1,3]))

def remove_duplicates(list1):
    A = list(set(list1))
    return A 

print(remove_duplicates([1,2,1,2,1,2,1,2]))
"""
# to check list empty or not
"""
def empty_or_not(list):
    if len(list) == 0:
        return"empty list"
    else:
        return("List is not empty")

print(empty_or_not([]))
print(empty_or_not([1,2,3]))

# clone or copy list
def clone_list(list1):
    list2 = list(list1)
    list2.append(5)
    return("list2 = ", list2,"list1=", list1)
print(clone_list([1,2,3,4]))

# to filter lists by length
def filter_by_length(list):
    if len(list) >= 3:
        return ("The list is too big", list)
    else:
        return(list)
print(filter_by_length([1,2,3,4,5]))
print(filter_by_length([6,7]))


def compare_list(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(compare_list([1,2,3,4,5],[5,6,7,8]))
print(compare_list([1,23],[3,4]))

#remove even numbers from list 
nums = [1,2,3,4,5,6,7,8,9,10]
nums = [i for i in nums if i % 2 != 0 ]
print(nums)

from random import shuffle
def shuffle_list(num):
     shuffle(num)
print(shuffle_list([1,2,3,4,5,6,7,8,9,10]))


def square_values():
    list1 = []
    for i in range(1,31):
        list1.append(i**2)
    a = (list1[:5])
    b = (list1[-5:])
    print(a + b)

square_values()























