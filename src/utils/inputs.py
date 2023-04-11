
from src.utils.console import *


def input_int(nrange):
    while True:
        try:
            uinp = int(input(f'[?] Select Option [1-{nrange}]> '))
        except ValueError:
            red("[!!] Not an ineteger. Please try again!")
        else:
            if (uinp < 1 or uinp > nrange):
                red("[!! Please enter a valid option!")
            else:
                break
    return uinp
