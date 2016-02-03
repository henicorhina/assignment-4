#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 03 February 2016 15:34 CST (-0600)
"""

import numpy
from Bio import Seq


def check_numpy_type():
    numbers = range(1, 5)
    print(type(numpy.array(numbers)))


def check_seq_type():
    seq = Seq.Seq('ACGT')
    print(type(seq))


def main():
    check_numpy_type()
    check_seq_type()

if __name__ == '__main__':
    main()
