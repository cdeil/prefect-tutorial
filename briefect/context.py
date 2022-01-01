import sys
import logging
from prefect.utilities.collections import DotDict


class Context(DotDict):
    """Context is a dict that allows dot access."""


# Global context that Prefect uses to coordinate things
# e.g. to register tasks with the DAG on flow definition
context = Context()


def _create_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Set the format from the config for stdout
    formatter = logging.Formatter(
        context.config.logging.format, context.config.logging.datefmt
    )
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.setLevel(context.config.logging.level)

    return logger


context.logger = _create_logger("prefect")
