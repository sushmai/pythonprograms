def FileCheck(fn):
    try :
        open(fn, "r")
        return 1
    except IOError :
        print ("Error : File does not exist.")
    return 0
result = FileCheck("testfile")
print(result)
