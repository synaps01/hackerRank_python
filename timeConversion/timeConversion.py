#!/bin/python3

import sys
import datetime

time = input().strip()
dtime = datetime.datetime.strptime(time, '%I:%M:%S%p')
print(dtime.strftime('%H:%M:%S'))
