#/usr/bin/env python

import colorama
from colorama import Fore, Back, Style

def calculate(string):
    stack = list()
    for token in string.split():
        if token == "+":
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 + arg2
            stack.append(result)
        elif token == "-":
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 - arg2
            stack.append(result)
        elif token == "^":
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 ** arg2
            stack.append(result)
        elif token == "*":
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 * arg2
            stack.append(result)
        else:
            stack.append(int(token))

        print(Back.GREEN + Fore.BLUE + Style.DIM +str(stack))
    if len(stack) != 1:
        raise TypeError("Malformed input: " + string)
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
    main()
