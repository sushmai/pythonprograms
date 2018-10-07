# Sort array to print even numbers first in order followed by odd numbers
class Solution:
    A = []
    def sortArray(self, A):

        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return (even + odd)


