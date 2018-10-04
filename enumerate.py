# enumerate returns a tuple contating a count from 0 
seasons = ['Spring', 'Summer', "Fall", "Autom"]

print(list(enumerate(seasons)))

# we can define count
print(list(enumerate(seasons, start = 1)))

# with function
def enumerate(sequence, start = 0 ):
    n = start
    for elem in sequence:
        yeild (n, elem)
        n += 1

