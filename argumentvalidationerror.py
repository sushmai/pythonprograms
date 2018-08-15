class ArgumentValidationError(ValueError):
    """
    Raised when the type of an argument to a function is not what it should be .
    """
    def __init__(self, arg_num, func_name, accepted_arg_type):
        self.error = "The {0} argument of {1}() is not A {2}". format(arg_num, func_name, accepted_arg_type)
        def __str__(self):
            return self.error

class InvalidArgumentNumberError(ValueError):
        """
        Raised when the number of argumnets supplied to a function is incorrect
        Note that this check is only performed from the number of argumnetd
        specified in the validate_accept() decorator. If the validate_accept()
        call is incorrect, it is possible to have a valid function where this will
        report a false validation.
        """
        def __init__(self, func_name):
            self.error = "Invalid number of arguments for {0}()". format(fun_name)

        def __str__(self):
            return self.error

class InvalidReturnType(ValueError):
    """
As The name implies, the return value is the wrong type.
"""
    def __init__(self, return_type, func_name):
        self.error = "Invalid return type {0} for {1}()". format(return_type, func_name)

    def __str__(self):
        return self.error

    def ordinal(num):
        """
returns the ordinal number of a given integer, as a string.
eg. 1 -> 1st, 2 -> 2nd, etc.
"""
        if 10 <= num % 100 < 20:
            return '{0}th'. format(num)
        else:
            ord = {1 : 'st', 2 : "nd", 3 : 'rd'}.get(num % 10, 'th')
            return '{0}{1}'. format(num, ord)
        
        
