#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.


def hackerlandRadioTransmitters(x, k):
    x = sorted(x)
    c = 1
    t = x[0]
    for i in range(len(x)):
        if x[i] == t + k:
            t = x[i]
        elif x[i] > t + k:
            t = x[i-1]
        else:
            continue
        for j in range(i, len(x)):
            if x[j] > t + k:
                t = x[j]
                c += 1
                break
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
