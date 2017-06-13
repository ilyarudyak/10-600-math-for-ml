def plus_one(f):
    return lambda x: f(x) + 1


def square(x):
    return x * x


if __name__ == '__main__':
    print(plus_one(square)(2))
