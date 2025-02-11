import logging
from enum import Enum

"""
- NOTSET    (0): This level captures all messages, regardless of their severity.
- DEBUG    (10): This level is used for anything that can help identify potential problems, like variable values or the steps that a program takes.
- INFO     (20): This level is used to confirm that things are working as expected.
- WARNING  (30): This level indicates that something unexpected happened, or there may be some problem in the near future (like 'disk space low'). However, the software is still working as expected.
- ERROR    (40): This level indicates a more serious problem that prevented the software from performing a function.
- CRITICAL (50): This level denotes a very serious error that might prevent the program from continuing to run.
"""

class LogLevel(Enum):
    DEBUG = logging.DEBUG  # 10
    INFO = logging.INFO  # 20
    WARNING = logging.WARNING  # 30
    ERROR = logging.ERROR  # 40
    CRITICAL = logging.CRITICAL  # 50


def console_logger(name: str, level: LogLevel) -> logging.Logger:
    # Create a named logger
    logger = logging.getLogger(f"__{name}__")
    logger.setLevel(level.value)  # Set logger level using enum value

    # Create a console handler and set its level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level.value)

    # Set the formatter for the console handler
    formatter = logging.Formatter(
        "\n%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S",
    )
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    return logger