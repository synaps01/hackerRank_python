#!/bin/python3

import sys


n = int(input().strip())
a = []
da = 0
db = 0
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)
   for a_j in range(n):
        if a_i == a_j:
                da += a[a_i][a_j]
        if a_j == ( n - 1 - a_i ):
            db += a[a_i][a_j]
print(str(abs(da - db)))

