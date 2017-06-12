import re


def ex4(str_set):
    return {s for s in str_set if is_valid(s)}


def is_valid(s):
    return re.match('^[a-mA-M]+$', s)


if __name__ == '__main__':
    example_set = {'cat', 'dig', 'dog', 'ant', 'eel'}
    print(ex4(example_set))
