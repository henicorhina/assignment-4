#!/usr/bin/env python
# encoding UTF-8

'''
Task2-based on previous, create another program with a main function that calls
separate function to print out the same information requested in task1.
'''
# calls on previous...


def previ():
    print(list(range(0, 51, 5)))

    def main():
        previ()
if __name__ == '__main__':
    main()
