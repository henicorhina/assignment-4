# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 4
Oscar Johnson 9 February 2016
"""

from Bio.Seq import Seq
import numpy as np

def seq_type(seq):
    """
    returns the sequence and the sequence type
    """
    return (seq, type(seq))


def array_type(array):
    """
    returns the array and the array type
    """
    return (array, type(array))


def main():
    my_array = np.array([0, 3, 5, 7])
    seq = Seq("ACGT")
    x = seq_type(seq)
    y = array_type(my_array)
    print (x, y)
    
if __name__ == '__main__':
    main()
