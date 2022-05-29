#!/usr/bin/env python
import pytz
from datetime import datetime as dt

kz = pytz.timezone('Asia/Seoul')
pz = pytz.timezone('US/Pacific')
bz = pytz.timezone('Europe/London')
zt = dt.utcnow()
lt = dt.now()

times = []
times.append(f'{zt}Z\t\tUTC')
times.append(f'{lt.astimezone(kz)}\tSeoul')
times.append(f'{lt.astimezone(pz)}\tSan Francisco')
times.append(f'{lt.astimezone(bz)}\tLondon')
for t in sorted(times, reverse=True):
    print(t)
