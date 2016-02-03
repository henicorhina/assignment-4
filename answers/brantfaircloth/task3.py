#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 03 February 2016 15:22 CST (-0600)
"""


def function1():
    print(", ".join([str(i) for i in range(0, 51, 5)][::-1]))


def main():
    function1()

if __name__ == '__main__':
    main()
