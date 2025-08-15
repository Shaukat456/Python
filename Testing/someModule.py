# This is a test module for demonstrating imports


def sum1(*args):
    total = 0
    for num in args:
        total += num
    print(total)


if __name__ == "__main__":
    print(sum1(1, 2, 3))
