#handler

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# file instantly creates 
handler = logging.FileHandler('info.log')
handler.setLevel(logging.INFO)

logger.addHandler(handler)


logger.info("Helpful logging message, id: {}".format(1))
logger.error("{} error encountered on line {}".format(keyError,10))


"""
helpful logging message, id : 1
<type 'excetions.KeyError'> error encountered on line 10 
"""
