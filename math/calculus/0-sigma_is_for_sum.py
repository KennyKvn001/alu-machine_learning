#!/usr/bin/env python3


def sigma(n):
    sum = 0
    for i in range(2, n + 1):
        sum += i
    return sum


print(sigma(5))
