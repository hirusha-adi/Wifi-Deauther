import sys


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def doing(*args, **kwargs):
    print(Colors.BLUE, *args, **kwargs)


def success(*args, **kwargs):
    print(Colors.GREEN, *args, **kwargs)


def error(*args, **kwargs):
    print(Colors.RED, *args, **kwargs)


def print_(*args, **kwargs):
    print(Colors.RESET, *args, **kwargs)
