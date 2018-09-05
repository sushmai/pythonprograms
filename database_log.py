import logging
logging.basicConfig(level - logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Start reading database")

records = {"Jon": 55, "Tom":66}
logger.debug("Records:%s", records)
logger.info("Updating records...")
logger.info("Finish Updating ")

"""
Output :
INFO:__main__:Start reading database :
INFO:__main__:Updating records...
INFO:__main__:Finish updating records
root@055104c7bd03:/# vi database_log.py


FOR DEBUG
root@055104c7bd03:/# python database_log.py
INFO:__main__:Start reading database :
DEBUG:__main__:Records: {'john': 55, 'tom': 66}
INFO:__main__:Updating records...
INFO:__main__:Finish updating records 
"""
