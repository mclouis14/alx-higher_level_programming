#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
result = islower('a')
print(result)
result = islower('A')
print(result)
