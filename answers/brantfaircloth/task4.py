#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 03 February 2016 15:31 CST (-0600)
"""


def my_favorite(words):
    for word in words:
        print(word)


def main():
    words = ["onomatapoeia", "persimmon", "grudge", "perfect", "original"]
    my_favorite(words)

if __name__ == '__main__':
    main()
