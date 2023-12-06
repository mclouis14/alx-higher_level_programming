#!/usr/bin/python3
#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = rom_num.get(char, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value
    return result
