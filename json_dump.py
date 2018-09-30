import json

data = {}
data['people'] = []
data['people'].append({
    'name':'Jon',
    'website':'Stackabuse.com',
    'from':"Alaska"
})
data['people'].append({
    'name':'larry',
    'website':'Google.com',
    'from':"Michigan"
})
data['people'].append({
    'Name':'Tim',
    'website':'apple.com',
    'from':'Alabama'
})
with open('data.txt', 'w') as outfile:
    #json.dump wriet the data to the outfile
    json.dump(data, outfile)
    
    
