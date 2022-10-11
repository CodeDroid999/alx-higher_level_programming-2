#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    prn = 0

    try:
        for i in my_list:
            if prn < x:
                print('{}'.format(my_list[prn]), end='')
                prn += 1

        print()
    except TypeError:
        pass
    finally:
        return prn
