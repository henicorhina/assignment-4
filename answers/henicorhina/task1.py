# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 4
Oscar Johnson 9 February 2016
"""

def main():
    """
    print a range of numbers from 0 to 50
    that are divisible by 5
    """
    for i in range(0,55,5):
        print (str(i) + ', ', end = '')

if __name__ == '__main__':
    main()
