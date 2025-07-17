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
    line_count = 0  # Counts ALL lines (valid + invalid)

    try:
        for line in sys.stdin:
            line_count += 1  # Count every input line

            try:
                parts = line.split()
                # Validate minimum components exist
                if len(parts) < 7:
                    continue

                # Attempt to parse status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update metrics if valid
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            except (ValueError, IndexError):
                # Skip metric updates but keep line count
                continue

            # Print after every 10 input lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Allow print on CTRL+C via finally block
        pass
    finally:
        # Final print (last set of metrics)
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
