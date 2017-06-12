def ex4(int_set):
    return {x for x in int_set if not is_divisible(x)}


def is_divisible(x):
    return x % 2 == 0 or x % 3 == 0 or x % 5 == 0


if __name__ == '__main__':
    example_set = {1, 2, 3, 4, 5, 6, 7}
    print(ex4(example_set))
