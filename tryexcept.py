import sys

try:
    f = open('mary.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError :
    print("Cloud not convert data to an integer.")
except :
    print("Unexpected error:", sys.exc_info()[0])
    raise
