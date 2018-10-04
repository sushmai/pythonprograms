# enumerate returns a tuple contating a count from 0 
seasons = ['Spring', 'Summer', "Fall", "Autom"]

print(list(enumerate(seasons)))

# we can define count
print(list(enumerate(seasons, start = 1)))




my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
"""
# with function
def enumerate(sequence, start = 0 ):
    n = start
    for elem in sequence:
        yeild (n, elem)
        n += 1
"""
list1 = ['eat', 'sleep', 'repeat']
for i in enumerate(list1):
    print(i)
for count, i in enumerate(list1, 100):
    print(count, i)
