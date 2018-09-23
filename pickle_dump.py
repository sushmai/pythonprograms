# Python pickle is used for "serialize" and "deserialize" python object

import pickle

number_of_data = int(input("Enter the number of data: "))
data = []

for i in range(number_of_data):
    raw = input("Enter data " + str(i)+' : ')
    data.append(raw)

file = open('important', 'wb')

# dump information to the file

pickle.dump(data, file)

file.close()

