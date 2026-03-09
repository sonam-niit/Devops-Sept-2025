import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

logging.debug("Debug logs")
logging.info("Info Log")
logging.warning("Warning Logs")
logging.error("Error Log")
logging.critical("Critical Log")

# Debug < Info < Warning < Error < Critical