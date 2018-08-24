s = "Methods are build in functions, specific to object types, executes left to right"
# capitalizes first letter of sentence
print(s.capitalize())

# takes total letters counts and for remaining adds at  the end and beginning
print(s.center(100, "*"))
# counts number of s are present leaves zero if none
print(s.count("s"))
print(s.count("none"))
#
print(map(s.count, s))
# matches with each letter in s and counts number of times it appeared
print(list(map(s.count, s)))
# how map works with lambda
temps = [("los Angles ", 22), ("berlin", 30), ("london", 20), ("canada", 13), ("New York", 23 )]
# now we want temperature in fahrenheit instead of celsius
c_to_f = lambda data:(data[0], data[1]*(9/5)+ 32)
print(list(map(c_to_f, temps)))