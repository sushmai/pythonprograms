import logging
import os

logging.basicConfig(level = os.environ.get("LOGLEVEL", "INFO"))

exit(main())
