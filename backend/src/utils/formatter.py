import logging
import time


class Formatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)

    def formatTime(self, record, datefmt=None):
        converted_time = self.converter(record.created)
        return self.default_msec_format % (time.strftime(self.default_time_format, converted_time), record.msecs)
