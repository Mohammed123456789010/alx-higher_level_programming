#!/usr/bin/python3
def square_matrixImap(matrrix=[]):
    return list(map(lambda x: list(map(lambda i: i**2, x)), matrix))
