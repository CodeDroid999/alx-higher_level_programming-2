#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i is not 8 or j is not 9:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j))
