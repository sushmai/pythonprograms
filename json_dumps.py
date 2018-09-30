import json

data = {'people':[{'name':'Scott', 'website':'stackabuse.com','from':'Scott'}]}

#dumps returns actual json object 
print(json.dumps(data,indent = 4))
