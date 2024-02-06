import logging

logger = logging.getLogger("wikipedia-app")
logger.setLevel(logging.DEBUG)

# Console Handler
console_handler = logging.StreamHandler()
console_format = logging.Formatter(
    "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)
console_handler.setFormatter(console_format)
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
