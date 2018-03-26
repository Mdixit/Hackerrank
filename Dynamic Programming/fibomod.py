#!/bin/python3

import sys

def fibonacciModified(t1, t2, n):
    while n > 2:
        
        t3 = t1 + (t2 * t2)
        t1 = t2
        t2 = t3
        n = n-1
    return t2

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
