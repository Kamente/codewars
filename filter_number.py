# https://www.codewars.com/kata/55b051fac50a3292a9000025

def filter_string(string):
    result = ""
    for to_filter in string:
        if to_filter.isdigit():
            result += to_filter
    return int(result)

mixed_value = input('enter mixed_string: ')
number = filter_string(mixed_value)
print(number)