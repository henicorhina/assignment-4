# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 4
Oscar Johnson 9 February 2016
"""

def funk1():
    """
    creates a list of numbers from 0 to 50
    that are divisible by 5
    """
    x = []
    for i in range(0,55,5):
        x.append(str(i))
    return x


def main():
    """
    reverses and prints the list from funk1
    """
    x = funk1()
    x.reverse()
    print (x)
    
if __name__ == '__main__':
    main()
