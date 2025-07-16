#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
Prints statistics every 10 lines and on keyboard interrupt (CTRL+C).
"""

import sys


def print_stats(total_size, status_counts):
    """Print the current statistics."""
    print("File size: {}".format(total_size))

    # Print status codes in ascending order
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    for code in valid_codes:
        if code in status_counts and status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def parse_line(line):
    """Parse a log line and return status code and file size."""
    try:
        # Split the line to extract status code and file size
        parts = line.split()
        if len(parts) < 7:
            return None, None
        
        # The format should be:
        # <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
        # We need to find the status code and file size at the end
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        
        # Check if status code is valid
        valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
        if status_code not in valid_codes:
            return None, file_size
            
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None


# Initialize variables
total_size = 0
status_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # Parse the log line
        status_code, file_size = parse_line(line)
        
        # Only process if we got a valid file size
        if file_size is not None:
            total_size += file_size
            line_count += 1
            
            # Update status code count if valid
            if status_code is not None:
                status_counts[status_code] = status_counts.get(
                    status_code, 0) + 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
