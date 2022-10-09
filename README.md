# timepy
Time stuffs

But seriously, print out the time in some timezones. 

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

