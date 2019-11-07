#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: Nov 2019
# This program is counts from 1000 to 2000


def count():
    loop_counter = 0

    for num in range(1000, 2001):
        loop_counter += 1
        print(num, end=(" " if loop_counter < 5 else "\n"))

        if loop_counter == 5:
            loop_counter = 0


if __name__ == "__main__":
    count()
