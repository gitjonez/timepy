#!/usr/bin/env python3
import os
import sys
from tabulate import tabulate
from datetime import datetime as dt
from argparse import ArgumentParser, Namespace
from zoneinfo import ZoneInfo, available_timezones, ZoneInfoNotFoundError
from typing import List, Tuple, Optional

description = '''
Display times in specified timezones or search timezones.
See https://docs.python.org/3/library/zoneinfo.html#data-sources
Sub commands: zones, search
<sub-command> -h  for more help.

Example: ./timepy.py zones America/Vancouver
'''


def get_times(args: Namespace):
    zones: List[str] = args.zone
    print(f'* get_times({args})')

    if len(zones) == 0 or zones == ['UTC']:
        # defaults
        if args.no_UTC:
            zones = ['US/Pacific']
        else:
            zones = ['UTC']
    if not args.no_UTC and 'UTC' not in zones:
        zones += ['UTC']

    # get times
    results: List[dt] = []
    for zone in zones:
        try:
            tz = ZoneInfo(zone)
            tzdt = dt.now().astimezone(tz)
            results += [tzdt]
        except ZoneInfoNotFoundError:
            print(f'zone: "{zone}" not found', file=sys.stderr)

    # format output and print
    table: List[Tuple[str, str, str]] = []
    headers = ('Zone', 'Name', 'Time')
    for r in sorted(results, key=str):
        dtstr = dt.strftime(r, '%Y-%m-%d %H:%M:%S%z')
        table += [(str(r.tzinfo), str(r.tzname()), dtstr)]
    tabulated = tabulate(table, headers=headers)
    print(tabulated)


def tzsearch(args: Namespace):
    '''Print sorted tz search results
        args.all bool:
            Print all time zones
        args.substring: List[str]
            Substring(s) to search for in available_timezones() -> set
            (Case insensitive)
    '''
    if len(args.substring) == 0:
        return  # nothing to do

    search_results: List[str] = []
    try:
        for tz in available_timezones():
            tz_lower = tz.lower()
            if args.all:
                search_results += [tz]
            else:
                for srch in args.substring:
                    if ' ' in srch:  # spaces are stored as '_' in timezones
                        srch = srch.replace(' ', '_')
                    if srch.lower() in tz_lower:
                        search_results += [tz]
    except ZoneInfoNotFoundError:
        print('Zone info not found in call to', end=' ', file=sys.stderr)
        print('call to zoneinfo.available_timezones()')
        sys.exit(os.EX_NOTFOUND)

    if len(search_results) == 0:
        print(f'No timezones found with substring(s): {args.substring}')
    else:
        for result in sorted(search_results):
            print(result)


def parse_args(modified_args: Optional[List[str]] = None) -> Namespace:
    '''Modified args are sent if defaults are not met,
       i.e. (send -h)
    '''
    parser = ArgumentParser(description=description)

    subparsers = parser.add_subparsers(help='commands')

    # search
    search_parser = subparsers.add_parser('search', help='Search timezones')
    search_parser.add_argument('-a',
                               '--all',
                               action='store_true',
                               help='List all timezones')
    search_parser.add_argument(
        'substring',
        nargs='*',
        help='Substring(s) to search (case insensitive)')
    search_parser.set_defaults(func=tzsearch)

    # times: print time in timezones
    tz_parser = subparsers.add_parser('zones', help='Timezones to print')
    tz_parser.add_argument('-u',
                           '--no-UTC',
                           action='store_true',
                           help='Supress reporting of UTC')
    tz_parser.add_argument('zone',
                           nargs='*',
                           default=['UTC'],
                           help='Timezone(s) to print')
    tz_parser.set_defaults(func=get_times)

    parsed_args = parser.parse_args(args=modified_args)
    print(f'* parsed_args: {parsed_args}')
    return parsed_args


def main():
    args = parse_args()
    if 'func' in args:
        args.func(args)
    else:
        args = parse_args(['zones'])
        get_times(args)


if __name__ == '__main__':
    main()