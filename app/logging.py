import logging

def setup_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)

    # Console handler for debugging output
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # File handler for saving logs to file
    fh = logging.FileHandler("app.log")
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger

logger = setup_logger()
