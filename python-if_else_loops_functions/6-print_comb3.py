#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i < 8 or j < 9:
            print("{:01d}{:01d}".format(i, j), end=", ")
        else:
            print("{:01d}{:01d}".format(i, j))
