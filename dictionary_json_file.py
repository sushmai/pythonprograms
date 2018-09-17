import json
d = {}
d["gravity"] = {
    "mediator":"gravitons",
    "relative strength" : "1",
    "range" : "infinity"
}

d["weak"] = {
    "mediator":"W/Z bosons",
    "relative strength" : "10^25",
    "range" : "10^-18"
}

d["electromagnetic"] = {
    "mediator":"photons",
    "relative strength" : "10^36",
    "range" : "infinity"
}

d["strong"] = {
    "mediator":"gluons",
    "relative strength" : "10^38",
    "range" : "10^-15"
}

print(d)
# covert the dictionary to string using json.dumps()
data = json.dumps(d)
print(type(data))
print(data)
# write to file
with open('4forces.json', 'w') as f :
    f.write(data)

# read from file
with open('4forces.json', 'r') as f:
    data = f.read()

d = json.loads(data)



