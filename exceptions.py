"""
objective :
    - write function that reads binary file and returns data.
    - Measure time required to do this.
"""
import logging
import time
# create logger with debug level 

logging.basicConfig(filename = "s.py", level = logging.DEBUG)
# use this to both excetions and time used
logger = logging.getLogger()

def read_file_timed(path):
    """ return th contents of the file at 'path' and measure time required """
    # record the time the method began
    start_time = time.time()
    try :
        # try to open binary file and return the contents
        f = open(path, mode='r')
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file = path, time = dt))
        #print(logger.info)

data = read_file_timed("file.txt")
