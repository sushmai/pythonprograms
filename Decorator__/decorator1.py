def wrap_with_prints(fn):
    #this will only happen when a function is decorated
    #with @wrap_with_prints is defined
    print('wrap_with_prints runs only once')

    def wrapped():
        #this will happen each time just before
        #this decorated function is called
        print('About to run %s ' % fn.__name__)
        #here is where the wrapper calls the decorated function
        fn()
        #this will happen each time just after
        #the decorated function is called
        print('Done running is %s' % fn.__name__)

    return wrapped

@wrap_with_prints
def func_to_decorate():
    print('Running the funciton that wasdecorated. ')

func_to_decorate()

"""
Note that the decorator (wrap_with_prints) runs only once, when the decorated function is created,
but the inner function (wrapped) runs each time you run func_to_decorate.
"""
