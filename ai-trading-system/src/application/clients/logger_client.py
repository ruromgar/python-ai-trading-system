import logging


class LoggerClient:

    _config = None

    def __init__(self, config):
        self._config = config.LOG_CONFIG

    def get_logger(self):
        logger = logging.getLogger(self._config['name'])
        logger.setLevel(self._config['level'])
        log_handler = self._config['stream_handler']
        formatter = logging.Formatter(self._config['format'])
        log_handler.setFormatter(formatter)
        logger.addHandler(log_handler)
        return logger
