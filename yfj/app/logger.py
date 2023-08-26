import logging

def configure_logging(app: Flask):
    # Set the log level
    log_level = logging.INFO  # You can adjust the log level as needed

    # Create a logger instance
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create a file handler
    log_file = 'app.log'  # Change to the desired log file name
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Create a console handler (for printing logs to console)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create a formatter and set it for the handlers
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    app.logger.addHandler(logger)
