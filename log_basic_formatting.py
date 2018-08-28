import logging

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.setHandler(handler)

logger.info("Log messager, id:{}".format(1))
logger.error("{} error encountered on line {}".format(keyError, 10))
