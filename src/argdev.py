#!/usr/bin/env python3
from zoneinfo import ZoneInfo
from argparse import ArgumentParser, Namespace
from typing import List

description = '''
Display times in specified timezones or search timezones.
'''
StrList = List[str]


def parse_args() -> Namespace:
    parser = ArgumentParser(description=description)

    subparsers = parser.add_subparsers(help='commands')

    # search
    search_parser = subparsers.add_parser('search', help='Search timezones')
    search_parser.add_argument('searchstr',
                               nargs='+',
                               type=StrList,
                               action='store',
                               help='Substring to search (case insensitive)')

    # times: print time in timezones
    tz_parser = subparsers.add_parser('zones', help='Timezones to print')
    tz_parser.add_argument('zone',
                           type=StrList,
                           nargs='*',
                           action='store',
                           help='Timezones to print')

    return parser.parse_args()


def main():
    args = parse_args()
    print('args:\n{args}')


if __name__ == '__main__':
    main()