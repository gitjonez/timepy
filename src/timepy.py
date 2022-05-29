#!/usr/bin/env python3
import pytz
import argparse
from datetime import datetime as dt

parser = argparse.ArgumentParser(description='Call time based on timezone')

parser.add_argument('-t',
                    '--timezones',
                    action='store_true',
                    help='List timezones')
parser.add_argument('-l',
                    '--location',
                    default='Vancouver',
                    help='Specify location[s]')

args = parser.parse_args()

zt = dt.utcnow()
lt = dt.now()

# Print UTC
print(f"UTC:\t{zt}Z")

# Search for tz on args:
for i in pytz.all_timezones:
    if args.timezones:
        print(f"{i}")
    elif args.location in i:
        print(f"{args.location}:\t{lt.astimezone(pytz.timezone(i))}")
