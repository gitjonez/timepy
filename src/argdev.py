#!/usr/bin/env python3
from re import I
from zoneinfo import ZoneInfo
from argparse import ArgumentParser, Namespace

description = '''
Display times in specified timezones or search timezones.
'''


def tzsearch(args: Namespace):
    print(f'tzsearch({args}) called')


def parse_args() -> Namespace:
    parser = ArgumentParser(description=description)

    subparsers = parser.add_subparsers(help='commands')

    # search
    search_parser = subparsers.add_parser('search', help='Search timezones')
    search_parser.add_argument('-a',
                               '--all',
                               action='store_true',
                               help='List all timezones')
    search_parser.add_argument('searchstr',
                               nargs='*',
                               help='Substring to search (case insensitive)')
    search_parser.set_defaults(func=tzsearch)

    # times: print time in timezones
    tz_parser = subparsers.add_parser('zones', help='Timezones to print')
    tz_parser.add_argument('zone', nargs='*', help='Timezones to print')

    return parser.parse_args()


def main():
    args = parse_args()
    print(f'args:\n{args}')
    args.func(args)


if __name__ == '__main__':
    main()