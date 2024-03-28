#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
file_sizes = {}
total_size = 0
lines_processed = 0

# Function to handle interrupt signal (CTRL+C)


def signal_handler(sig, frame):
    """ Signal function """
    print_statistics()
    sys.exit(0)

# Function to print statistics


def print_statistics():
    """ Statistics function """
    print(f"Total file size: {total_size}")
    for status_code in sorted(file_sizes.keys()):
        print(f"{status_code}: {file_sizes[status_code]}")


# Register the signal handler for interrupt
signal.signal(signal.SIGINT, signal_handler)

# Process lines from stdin
for line in sys.stdin:
    try:
        # Split line by spaces
        parts = line.split()

        # Extract status code and file size
        status_code = int(parts[-2])
        size = int(parts[-1])

        # Update total file size
        total_size += size

        # Update file sizes dictionary
        file_sizes[status_code] = file_sizes.get(status_code, 0) + 1

        # Increment lines processed
        lines_processed += 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print_statistics()
    except Exception as e:
        # Skip invalid lines
        continue

# Print final statistics
print_statistics()
