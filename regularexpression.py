# extract from particulat data from string
"""
Regular expression
^ Start
$ Stop
. Any Character
* Match one character  0 + times
+ match one character 1 + times
\s whitespace
\S non-WhiteSpace
[abc] match one character in the specified set
[^abc] match one chatacter not in the specified set 
"""
import re

myString = "A regular expression is a special 23 "
print(myString)
    
d = re.findall('^A', myString)
e = re.findall('$g', myString)
f = re.findall('.', myString)

a = re.findall('[0-9]+', myString)
b = re.findall('[^abc]+', myString)
c = re.findall('\S+', myString)
result = re.findall('[abc]', myString)
s = re.findall('\s', myString)

print('^A = ', d)
print('$g = ', e)
print('.=', f)
print('+', a)
print('^abc =', b)
print('\S',c)
print('\s',s)
print(result)
