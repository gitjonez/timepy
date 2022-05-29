#!/usr/bin/env python3
import pytz
from datetime import datetime as dt
tzs = {'Seoul' : 'Asia/Seoul', 'San Francisco' : 'US/Pacific', 'London' : 'Europe/London'}

zt = dt.utcnow()
lt = dt.now()

# Print UTC
print(f"{zt}Z\t\tUTC \n")

# Print time in dict.
for a in tzs:
    print(f"{lt.astimezone(pytz.timezone(tzs[a]))}\t{a}")

