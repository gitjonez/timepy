#!/usr/bin/env python3
import os
import sys
from tabulate import tabulate
from datetime import datetime as dt
from argparse import ArgumentParser, Namespace
from zoneinfo import ZoneInfo, available_timezones, ZoneInfoNotFoundError
from typing import List, Tuple

description = '''
Display times in specified timezones or search timezones.
See https://docs.python.org/3/library/zoneinfo.html#data-sources
'''


def get_times(args: Namespace):
    zones: List[str] = args.zone

    if len(zones) == 0:
        # defaults
        if args.no_UTC:
            zones = ['US/Pacific']
        else:
            zones = ['UTC']
    else:
        zones += ['UTC']

    results: List[dt] = []
    for zone in zones:
        try:
            tz = ZoneInfo(zone)
            tzdt = dt.now().astimezone(tz)
            results += [tzdt]
        except ZoneInfoNotFoundError:
            print(f'zone: "{zone}" not found')

    table: List[Tuple[str, str, str]] = []
    headers = ('Zone', 'Name', 'Time')
    for r in sorted(results):
        table += [(str(r.tzinfo), str(r.tzname()), str(r))]
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


def parse_args() -> Namespace:
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
    tz_parser.add_argument('zone', nargs='*', help='Timezone(s) to print')
    tz_parser.set_defaults(func=get_times)

    return parser.parse_args()


def main():
    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()