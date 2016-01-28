#!/usr/bin/env python
# encoding UTF-8

'''
task6-write a program with a main function that calls two separate functions to
the type of (1)a numpy array, and (2)a sequence object (from biopython).
'''


import biopython
import numpy


def main():
    print(type(numpy.array))
    print(type(biopython.seq))


if __name__ == '__main__':
    main()
