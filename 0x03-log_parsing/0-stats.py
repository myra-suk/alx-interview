#!/usr/bin/python3
"""
The module contains a script that reads stdin line by line and computes metrics
"""

import sys


def print_stats(file_size, status_codes):
    """
    Print file size and status codes
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            tokens = line.split()
            file_size += int(tokens[-1])
            if tokens[-2] in status_codes:
                status_codes[tokens[-2]] += 1
            if counter % 10 == 0:
                print_stats(file_size, status_codes)
        print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
