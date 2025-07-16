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
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    
    try:
        for line in sys.stdin:
            line = line.strip()
            
            # Parse the line manually to handle wrong format gracefully
            try:
                # Split by quotes to get the method part
                parts = line.split('"')
                if len(parts) >= 3:
                    # Check if middle part is the expected GET request
                    if parts[1] == "GET /projects/260 HTTP/1.1":
                        # Split the last part to get status code and file size
                        after_quote = parts[2].strip().split()
                        if len(after_quote) >= 2:
                            status_code = int(after_quote[0])
                            file_size = int(after_quote[1])
                            
                            # Update total file size
                            total_size += file_size
                            
                            # Update status code count if valid
                            if status_code in status_counts:
                                status_counts[status_code] += 1
                            
                            line_count += 1
                            
                            # Print stats every 10 lines
                            if line_count % 10 == 0:
                                print_stats(total_size, status_counts)
            except (ValueError, IndexError):
                # Skip lines with wrong format
                continue
    
    except KeyboardInterrupt:
        pass
    finally:
        # Print final stats
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
