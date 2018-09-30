# json.dump will encode all text given to dictionary to ASCII-encoded,
# if Non-ascii charecters are present the are escaped automaticallu

import json
data = {'item': 'Beer', 'cost':'£34.00'}
jstr = json.dumps(data, ensure_ascii = True, indent = 4)
print(jstr)

"""
OutPut:
    {
    "item": "Beer",
    "cost": "\u00a334.00"
    }
"""
