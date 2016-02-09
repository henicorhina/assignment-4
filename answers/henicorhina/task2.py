# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 4
Oscar Johnson 9 February 2016
"""

def funk1():
    """
    prints a string of numbers from 0 to 50
    that are divisible by 5
    """    
    for i in range(0,55,5):
        print (str(i) + ', ', end = '')


def main():
    print (funk1())
    
if __name__ == '__main__':
    main()
