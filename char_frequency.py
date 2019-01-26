from collections import Counter
test_str = "google.com"
res  = Counter(test_str)
print(str(res))

def char_frequency(str1):
    res1 = Counter(str1)
    return str(res1)
print(char_frequency("Hello"))

# using dict.get()
str2 = "another method"
res = {}
for keys in str2:
    res[keys] = res.get(keys, 0) + 1
print(str(res))


# using set() and count()
str3 = "Yet another method"
res = {i : str3.count(i) for i in set(str3)}
print(str(res))
"""
def char_frequency(str1):
    dict  = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency("Hello"))
print(char_frequency("google.com"))

"""


