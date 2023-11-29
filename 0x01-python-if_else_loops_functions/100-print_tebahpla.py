#!/usr/bin/python3
for char in range(ord('Z'), ord('a') - 1, -1):
    print("{:c}".format(char), end='')
