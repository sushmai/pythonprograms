import statistics

data = [1,2,3,4,5,6,7,8,9]
avg = statistics.mean(data)
print(avg)
print(filter(lambda x : x > avg, data))
print(list(filter(lambda i : i > avg, data)))

# we can remove null values form list using filter
# treats 0, (), {},0.0, 0j, [], False as none or null - but sometimes zero is a value

countries = ["", "India", "USA", "", "Brazil", "", "Canada", "Mexico", "Colombia" ""]
print(countries)
print(list(filter(None, countries)))
