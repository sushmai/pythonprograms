# to achive ordering we can use sorting

import json
data = {'people':[{'name':'Scott', 'website':'stackabuse.com', 'from':'Scott'}]}

# ca use sort_keys = True using json.dump or json.dumps
print(json.dumps(data, sort_keys = True, indent = 4))
