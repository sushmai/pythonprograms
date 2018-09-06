#import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create A file handler

handler = logging.FileHandler("Hello.log")
handler.setLevel(logging.INFO)

# Create logging Format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# add the handler to logger
logger.addHandler(handler)
logger.info("Hello")




"""
output: creatses a hello.log file 
    2018-09-06 03:29:56, 540 -__main__ - INFO - hello

    #####
out put will be repeated and preovious out will available for repeated executions.

"""
