#!/usr/bin/python3
import re
import sys


def print_stats(total_size, status_counts):
    """Print current statistics"""
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


def parse_log_line(line):
    """Parse a log line and return (status_code, file_size) or None if invalid"""
    # Regex pattern for the exact format required
    pattern = (r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] '
               r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')
    
    match = re.match(pattern, line.strip())
    if not match:
        return None
    
    ip, status_code, file_size = match.groups()
    
    # Validate IP address components (each should be 0-255)
    ip_parts = ip.split('.')
    for part in ip_parts:
        if not (0 <= int(part) <= 255):
            return None
    
    # Validate status code is in allowed list
    allowed_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    if status_code not in allowed_status_codes:
        return None
    
    return int(status_code), int(file_size)


# Main processing logic
total_size = 0
status_counts = {}
line_count = 0

try:
    for line in sys.stdin:
        parsed = parse_log_line(line)
        if parsed:  # Only process valid lines
            status_code, file_size = parsed
            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
            line_count += 1
            
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_counts)
