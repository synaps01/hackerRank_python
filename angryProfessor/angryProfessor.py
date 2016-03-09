#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    on_time = 0
    for i in a:
        if i <= 0:
            on_time += 1
            if on_time >= k:
                print("NO")
                break
    if on_time < k:
        print("YES")
