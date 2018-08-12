def log_calls(fn):
    '''wraps fn in a function named 'inner' that writes
        the argumnets and return value to logfile.log'''
    def inner(*args, **kwargs):
        # call the funcion with the received arguments and
        #keyword arguments, storing the return value
        out = apply(fn, args, kwargs)

        #write a line with the function name, its
        #arguments, and its return value to the log file

        with open('logfile.log', 'a') as logfile:
            logfile.write('%s called with args %s and kwars %s, returning %s\n' % (fn.__name__, args, kwargs, out))

            #return the return value
            return out
        return inner

@log_calls
def fizz_buzz_or_number(i):
    """ Return "fizz" if i is divisible by 3, "buzz" if by 5, and
        'fizzbuzz' if both, otherwise, return i."""
    if i % 15 == 0:
        return 'fizzbuzz'
    elif i % 3 == 0:
        return 'fizz'
    elif i % 5 == 0:
        return 'buzz'
    else:
        return i

for i in range(1,31):
    (print(fizz_buzz_or_number(i)))()            
