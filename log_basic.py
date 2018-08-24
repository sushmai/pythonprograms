import logging
import math
# create and configure logger
# basic config is one of the logging method
# pass the file name - it will pass all the logdata to that file if file doesnot exists python will create it
# debug to see all log messages
#to see log time
#FORMAT = "%(Levelname)d %(asctime)d - %(message)d"
# add format for basic format call
logging.basicConfig(filename = "log.log", level = logging.DEBUG)

# call the getlogger method to create logger object, can even pass a name to logger as argument
logger = logging.getLogger()
# test the logger
logger.info("Our first message.")

print(logger.level)

#function implementing quadratic formula to solve equation :

def quadratic_formula(a,b,c):
    """ return the solutions to the equation ax^2 + bx + c = 0. """

    logger.info("quadratic_formula({0}, {1},{2}".format(a,b,c))

    # compute the discriminant
    logger.debug("#compute the discriminant.")
    disc = b**2 - 4*a*c

    #compute the two roots
    logger.debug("# compute the two roots.")
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # return the roots
    logger.debug("return the roots")
    return (root1, root2)
roots = quadratic_formula(1,0,-4)
print(roots)




