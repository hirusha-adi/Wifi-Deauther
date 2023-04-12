import sys


class _Colors:
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


def blue(*args, **kwargs):
    print(_Colors.BLUE, *args, **kwargs)


def green(*args, **kwargs):
    print(_Colors.GREEN, *args, **kwargs)


def yellow(*args, **kwargs):
    print(_Colors.YELLOW, *args, **kwargs)


def red(*args, **kwargs):
    print(_Colors.RED, *args, **kwargs)


def print_(*args, **kwargs):
    print(_Colors.RESET, *args, **kwargs)
