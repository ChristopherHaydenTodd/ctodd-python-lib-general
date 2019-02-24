#!/usr/bin/env python3
"""
    Purpose:
        Get User Input

    Steps:
        - Prompt for Input
        - Parse Input

    example script call:
        python3 get_user_input.py
"""

# Python Library Imports
import logging
import os
import sys

# Local Library Imports
from general_helpers import user_input_helpers


def main():
    """
    Purpose:
        Produce to a Kafka Topic
    """
    logging.info("Starting Get User Input")

    for user_input in user_input_helpers.get_input_from_user(max_input=999):
        logging.info(f"User Input: {user_input}")

    logging.info("Get User Input Complete")


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[get_user_input] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        logging.exception(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err
