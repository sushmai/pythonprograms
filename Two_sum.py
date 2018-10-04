"""
return the indices of two numbers

example : given numbers - [2,7,11,15] , target = 9

because numbers[0] + numbers[1] = 2+7 = 9

return [0,1]


"""

class solution:
    def twoSum(self, nums, target)
    """
    :type nums : list[int]
    :type target : int
    :rtype : list[int]

"""
    a = []
    for i, n in enumerate(nums):
        if a.get(n) is not None:
            return [a[n], i ]
        a[target-n] = i
    return null 
