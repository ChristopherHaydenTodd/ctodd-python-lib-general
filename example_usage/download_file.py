#!/usr/bin/env python3
"""
    Purpose:
        Download A File

    Steps:
        - Get data from URL
        - Parse Where to Store
        - Download File

    example script call:
        python3 download_file.py {--url=url}

    Note:
        https://www.thinkbroadband.com/download is a helpful link for
        getting test files of various sizes to download and test with
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
from general_helpers import downloader


def main():
    """
    Purpose:
        Starting Download File
    """
    logging.info("Starting Download File")

    opts = get_options()

    # downloaded_file = downloader.download_file(opts.url, overwrite=True)
    # downloaded_file = downloader.download_file(
    #     opts.url, file_location="./data/", overwrite=True
    # )
    downloaded_file = downloader.download_file(
        opts.url, file_location="./data/downloaded.zip", overwrite=True
    )

    logging.info("Download File Complete")


###
# General/Helper Methods
###


def get_options():
    """
    Purpose:
        Parse CLI arguments for script
    Args:
        N/A
    Return:
        N/A
    """

    parser = ArgumentParser(description="Download File")
    required = parser.add_argument_group("Required Arguments")
    optional = parser.add_argument_group("Optional Arguments")

    # Optional Arguments
    # N/A

    # Required Arguments
    required.add_argument(
        "-U", "-u", "--url",
        dest="url",
        help="URL to Download",
        required=True,
        type=str,
    )

    return parser.parse_args()


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[download_file] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        logging.exception(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err
