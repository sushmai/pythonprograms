# create dictionary
new_dict = {'key': 'value' , "1":'one', 'one':1}

#print dictionary
print(new_dict)

# read from dictionay
print(new_dict['key'])

# traverse through dictionary
for k,v in new_dict.items():
    print("the key is : %s" % k)
    print("the value is : %s" %v)
    print("**********************")

# add elements to blank dictionary

dict1 = {}
dict1['dog'] = 'barks'
dict1['cat'] = 'walks'
print(dict1)

# join two dictionaries

new_dict.update(dict1)
print(new_dict)

# delete elements from dictionary

del new_dict['key']
print(new_dict)

# check presence of key
print('1' in new_dict)
print('lids' in new_dict)
print('dog' in dict1)
