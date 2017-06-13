def filter_p(iset, p=lambda x: x ** 2 - x >= 5):
    return {x for x in iset if p(x)}


if __name__ == '__main__':
    int_set = {2, 3}
    print(filter_p(int_set))
