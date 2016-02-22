__author__ = 'rene_esteves'

import data_structure.util as util

def decimal_to_binary(input):
    if input <= 0: #base case
        return 0
    else:
        decimal_to_binary(int(input/2))  #recursive call
        print(str(input) + ' = ' + str(input%2))
        return input%2


def factorial(input):
    if input < 1: #base case
        return 1
    else:
        return input * factorial(input -1)  #recursive call

def sum(input):
    if input == 1: #base_case
        return 1
    else:
        return input + sum(input-1) #recursive call