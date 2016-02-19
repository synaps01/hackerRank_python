#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0
neg = 0
zer = 0
for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zer +=1
print(str(pos/n))
print(str(neg/n))
print(str(zer/n))

