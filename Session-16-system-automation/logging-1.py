import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    #level= logging.DEBUG
)

logging.debug("Checking bean grinder RPMs")
logging.info("Order #123 completed")
# Default level of log is warning
logging.warning("Low Milk Supply")
logging.error("Frother malfunction")
logging.critical("Power outage! Closing shop.")

# Seq of log levels
# Debug < Info < warning < error < critical