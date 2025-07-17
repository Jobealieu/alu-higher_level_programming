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
            line = line.strip()
            if not line:
                continue
            
            try:
                # Expected format: 
                # <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
                parts = line.split()
                
                # Check if line has enough parts
                if len(parts) < 7:
                    continue
                
                # Check if the request method part is correct
                if len(parts) >= 6 and parts[5] == '"GET' and \
                   parts[6] == '/projects/260' and parts[7] == 'HTTP/1.1"':
                    
                    status_code = int(parts[8])
                    file_size = int(parts[9])
                    
                    total_size += file_size
                    
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                    
                    line_count += 1
                    
                    if line_count % 10 == 0:
                        print_stats(total_size, status_counts)
                        
            except (ValueError, IndexError):
                continue

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
