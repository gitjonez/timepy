#!/usr/bin/env python3
import os
import sys
from zoneinfo import ZoneInfo, available_timezones, ZoneInfoNotFoundError
from argparse import ArgumentParser, Namespace
from typing import List

description = '''
Display times in specified timezones or search timezones.
See https://docs.python.org/3/library/zoneinfo.html#data-sources
'''


def get_times(args: Namespace):
    print(f'Debug: get_times() called with:\n{args}')
    print('get_times() not implemented')


def tzsearch(args: Namespace):
    '''Print sorted tz search results
        args.all bool:
            Print all time zones
        args.substring: List[str]
            Substring(s) to search for in available_timezones() -> set
            (Case insensitive)
    '''
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

    return parser.parse_args()


def main():
    args = parse_args()
    print(f'args:\n{args}')
    args.func(args)


if __name__ == '__main__':
    main()