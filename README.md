# timepy
Time stuffs

But seriously, print out the time in some timezones. 
New! With timezone search feature:

`❯ ./timepy.py -h`
```
usage: timepy.py [-h] {search,zones} ...

Display times in specified timezones or search timezones. See
https://docs.python.org/3/library/zoneinfo.html#data-sources

positional arguments:
  {search,zones}  commands
    search        Search timezones
    zones         Timezones to print

options:
  -h, --help      show this help message and exit
```
`❯ ./timepy.py zones -h`
```
usage: timepy.py zones [-h] [-u] [zone ...]

positional arguments:
  zone          Timezone(s) to print

options:
  -h, --help    show this help message and exit
  -u, --no-UTC  Supress reporting of UTC
```
`❯ ./timepy.py search -h`
```
usage: timepy.py search [-h] [-a] [substring ...]

positional arguments:
  substring   Substring(s) to search (case insensitive)

options:
  -h, --help  show this help message and exit
  -a, --all   List all timezones
```
`❯ ./timepy.py zones Europe/London Asia/Seoul US/Pacific America/New_York`
```
Zone              Name    Time
----------------  ------  --------------------------------
US/Pacific        PDT     2022-10-09 01:41:02.567057-07:00
America/New_York  EDT     2022-10-09 04:41:02.569292-04:00
UTC               UTC     2022-10-09 08:41:02.570019+00:00
Europe/London     BST     2022-10-09 09:41:02.563748+01:00
Asia/Seoul        KST     2022-10-09 17:41:02.566289+09:00
```

## Requirements
- python 3.9+
- tabulate

_See [`tzdata` IANA Datasource info](https://docs.python.org/3/library/zoneinfo.html#data-sources)_,
particularly if you are not finding a known timezone.

## Running
`python src/timepy.py`

## Installation
A possiblity:

`cp src/timepy.py <somewhere-in-your-path>/`
e.g. `cp src/timepy.py ~/bin/timepy`

## Notes 
### Time travel
"time has changed" and `pytz` depricated in python 3.9
Ok, maybe not deprecated, but no longer required:
Now in the standard library

