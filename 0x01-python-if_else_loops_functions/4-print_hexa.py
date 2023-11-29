#!/usr/bin/python3
"""print numbers 0 to 98 in decimal and hexadecimal."""
for num in range(99 + 1):
    print("{:d} = 0x{:x}".format(num, num), end='\n')
