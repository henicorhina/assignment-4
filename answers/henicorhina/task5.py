# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 4
Oscar Johnson 9 February 2016
"""

def favs(words):
    """
    prints words from a list
    """
    for word in words:
        print(word)
    
def main():
    """
    lists my five favorite words
    prints them using the favs function
    """
    my_favorite_words = ["bird", "python", "headbanging", "tropics", "beach"]
    favs(my_favorite_words)

if __name__ == '__main__':
    main()
