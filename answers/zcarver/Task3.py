#!/usr/bin/env pyhton
# encoding UTF-8

'''
task3-modify the prog you created in task2 to print the numbers in reversed
order.
'''
# prints previ in the reversed order
# [stackoverflow.com/questions/7286365/print-a-list-in-reverse-order-with-range-in-python]


def previrev():
    print(list(reversed(range(0, 51, 5))))

    def main():
        previrev()
if __name__ == '__main__':
    main()
