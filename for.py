"""
for i in range(0, 5):
    print (i)

for i in range(0, 10, 2):
    print (i)

for i in range(10, 0, -1):
    print (i)

for i in range(10, 0, -2):
    print (i)
"""
# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!

def show_excitement():
    for i in range(5):
        return ("I am super excited to learn this course" + ' ')
           
print(show_excitement() * 5)
