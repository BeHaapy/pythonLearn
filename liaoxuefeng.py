from functools import reduce


def plusOne(x):
    return x + 1


def plus(x, y):
    return x + y


def is_odd(x):
    return x % 2


if __name__ == '__main__':
    lists = [1, 2, 3, 4, 5]
    r = list(map(plusOne, lists))
    print(r)

    r = reduce(plus, lists)
    print(r)

    r = filter(is_odd, lists)
    print(list(r))
