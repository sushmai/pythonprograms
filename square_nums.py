def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
my_nums = square_numbers([1,2,3,4,5])
print(my_nums)


# write the above using generator
"""
generators does not hold the entire result in memory and yeild one result at a time

"""
def square_nums(nums):
    for i in nums:
        yield(i * i)
# nothing will be printed until we call - generator object value will be generated here
print(square_nums([6,7,8,9]))

# the computation waits to till we ask for the result "yield"
sq_num = square_nums([6,7,8,9])
# prints the suare of  first item from the list
print(next(sq_num))
# we need to call as many times as we need it
print(next(sq_num))
print(next(sq_num))
print(next(sq_num))
#stopiteration will be called by default and throughs an error
#print(next(sq_num))

"using for with yield"
sq_nums1 = square_nums([1,2,3,4])
for num in sq_nums1:
    print(num)

# using list comprehension
numbers = [x * x for x in [10,11,12]]
print(numbers)
for a in numbers:
    print(a)
    
