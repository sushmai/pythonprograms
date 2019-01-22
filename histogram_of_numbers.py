def histogram(numbers):
    for n in numbers:
        output = ""
        numbers  = n
        while(numbers > 0):
            output += "*"
            numbers = numbers -1
        print(output)

histogram([1,2,3,2,1])
