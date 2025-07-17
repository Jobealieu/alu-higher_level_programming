#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """Print current statistics"""
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def main():
    """Main function to process stdin and compute metrics"""
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            
            # Skip if we don't have enough tokens for status/size
            if len(parts) < 2:
                continue

            try:
                # Attempt to parse status code and file size from last two tokens
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Print after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass
    finally:
        # Final print on exit
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
