#!/usr/bin/python3

""" Functions that validate utf-8 encoding"""


def validUTF8(data):

    def checkLeadingOnes(byte, count):
        mask = 1 << (8 - count)
        return (byte & mask) == mask and (byte & (mask >> 1)) == 0

    remaining_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # If we are expecting more bytes for the current character
        if remaining_bytes > 0:
            # Check if the current byte starts with '10'
            if (byte >> 6) == 0b10:
                remaining_bytes -= 1
            else:
                return False
        else:
            """ Count the number of leading ones to determine the number of
            bytes for the character"""
            leading_ones = 0
            while (byte & (0x80 >> leading_ones)) != 0:
                leading_ones += 1

            # If the byte starts with '0', it is a single-byte character
            if leading_ones == 0:
                continue
            # If the byte starts with '110', it is a two-byte character
            elif leading_ones == 2:
                remaining_bytes = 1
            # If the byte starts with '1110', it is a three-byte character
            elif leading_ones == 3:
                remaining_bytes = 2
            # If the byte starts with '11110', it is a four-byte character
            elif leading_ones == 4:
                remaining_bytes = 3
            else:
                # Invalid leading ones count
                return False

            # Check if the remaining bytes start with '10'
            if not checkLeadingOnes(byte, leading_ones):
                return False

    # Check if all multi-byte characters are complete
    return remaining_bytes == 0
