#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import re

def print_stats(total_size, status_counts):
    """Print current statistics"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    
    # Regular expression to match the log format
    log_pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    
    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(log_pattern, line)
            
            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
                
                # Update total file size
                total_size += file_size
                
                # Update status code count if it's a valid status code
                if status_code in status_counts:
                    status_counts[status_code] += 1
                
                line_count += 1
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
    
    except KeyboardInterrupt:
        pass
    finally:
        # Print final stats
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
