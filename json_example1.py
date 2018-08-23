book = {}
book ['tom'] = {
    'name': 'tom',
    'address': 'red, ny',
    'phone': 3848372
}

book ['bob'] = {
    'name': 'bob',
    'address':'green, ny',
    'phone':353432
}

import json
s = json.dumps(book)
print(s)
with open('book.txt', 'w') as f:
    f.write(s)
