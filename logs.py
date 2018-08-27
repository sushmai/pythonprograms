import logging

format = "%(asctime)s[%(levels)s] %(message)s"
logger = logging.getLogger('example')
# can change 'debug or warning or info as per needs it is easier way to debug and find the errors'
logging.basicConfig(format=format,level = logging.DEBUG)

# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10 

class Item(object):
    """Base Item class"""

    def __init__(self, name, value):
        self.name = name
        self.value = value
        logger.info("Item created: {}({})".format(self.name, self.value))
    def buy(self, quantity = 1):
        """ Buy item """
        logger.debug("Bought item {}".format(self.name))

    def sell(self, quantity = 1):
        """sells items"""
        logger.warn("Sold item {}".format(self.name))
items = []
for index in xrange(100):
    items.append(Item('sword_'+str(index), 100))
for item in items:
    item.buy()
for item in items:
    item.sell()

item_01 = Item('sword', 150)
item_01.buy()
item_01.sell()
