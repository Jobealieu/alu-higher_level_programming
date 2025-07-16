#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
Prints statistics every 10 lines and on keyboard interrupt (CTRL+C).
"""

import sys
import signal


def print_stats(total_size, status_counts):
    """Print the current statistics."""
    print("File size: {}".format(total_size))

    # Print status codes in ascending order
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    for code in valid_codes:
        if code in status_counts and status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def signal_handler(signum, frame):
    """Handle keyboard interrupt (CTRL+C)."""
    print_stats(total_size, status_counts)
    sys.exit(0)


# Initialize variables
total_size = 0
status_counts = {}
line_count = 0

# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # Parse the log line
        # Format: <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
        try:
            # Split the line to extract status code and file size
            parts = line.split()
            if len(parts) >= 2:
                status_code = int(parts[-2])  # Second to last element
                file_size = int(parts[-1])    # Last element

                # Update total file size
                total_size += file_size

                # Update status code count (only for valid codes)
                valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
                if status_code in valid_codes:
                    status_counts[status_code] = status_counts.get(
                        status_code, 0) + 1

                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

        except (ValueError, IndexError):
            # Skip malformed lines
            continue
            
except KeyboardInterrupt:
    # This should be handled by the signal handler, but just in case
    print_stats(total_size, status_counts)
