#!/usr/bin/python3
"""scripts that reads stdin"""


import sys


def compute_metrics():
    """
    Read stdin line by line and compute metrics based input format.

    Metrics computed:
    - Total file size: Sum of file sizes encountered.
    - Number of lines by status code: Counts the occurrences of status code.

    Prints the computed statistics upon keyboard interruption.
    """
    # Initialize variables
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            # Remove leading and trailing whitespace from the line
            line = line.strip()

            # Parse the line
            ip_address, _, _, status_code, file_size = line.split()[0:5]

            # Update total file size
            total_size += int(file_size)

            # Update status code counts
            if status_code not in status_counts:
                status_counts[status_code] = 1
            else:
                status_counts[status_code] += 1

            # Check if 10 lines have been processed
            if i % 10 == 0:
                print("Total file size:", total_size)
                for code in sorted(status_counts.keys()):
                    print(code + ":", status_counts[code])

    # Handle keyboard interruption (CTRL + C)
    except KeyboardInterrupt:
        print("Total file size:", total_size)
        for code in sorted(status_counts.keys()):
            print(code + ":", status_counts[code])
