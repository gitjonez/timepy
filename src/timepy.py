#!/usr/bin/env python3
import pytz
import argparse
import sys

from datetime import datetime as dt

zt = dt.utcnow()
lt = dt.now()

# Print UTC
print(f"{zt}Z\t\tUTC")

# Search for tz on args:
count = 0
while count != len(sys.argv) - 1:
    count += 1
    for i in pytz.all_timezones:
        if sys.argv[count] in i:
            print(f"{sys.argv[count]}:\t{lt.astimezone(pytz.timezone(i))}")
