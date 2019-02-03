def my_gen():
    n = 1
    print("This printed first")
    # Generator function containts at least one yield statement
    yield n

    n += 1
    print("Print this next - 2")

    n += 1
    print("print this - 3")
    yield n

a = my_gen()
next(a)
