# Ticket Universe

[![CircleCI](https://circleci.com/gh/lotify/ticket_universe/tree/master.svg?style=svg)](https://circleci.com/gh/lotify/ticket_universe/tree/master)

A command line interface and library to generate a universe of unique ticket codes in Python 3.x.

## Installation
Ticket Universe can be installed via pip:

`pip install ticket-universe`

## Usage
Ticket Universe can be used as library and as command line interface.

### Command line interface
The ticket universe cli provides a means to generate a universe and write
it to stdout.

```
usage: ticket-universe [-h] [--offset OFFSET] [--limit LIMIT]
                       [POSITION [POSITION ...]]

example: ticket-universe fixed:LTFY- alpha numeric numeric numeric

positional arguments:
  POSITION         alpha | alpha:safe_latin | numeric | range:min:max |
                   fixed:{} | binary

optional arguments:
  -h, --help       show this help message and exit
  --offset OFFSET
  --limit LIMIT
```


### Library
```python
from ticket_universe.position import FixedPosition, AlphaPosition, NumericPosition, RangedPosition
from ticket_universe.universe import Universe


standard_universe = Universe([
    FixedPosition('LTFY-'),
    AlphaPosition(),
    NumericPosition(),
    NumericPosition()
])

# ['LTFY-A00', ..., 'LTFY-Z99']
print([t for t in standard_universe])


# Alternate charsets for alpha positions
charset_universe = Universe([AlphaPosition('safe_latin'), AlphaPosition('safe_latin')])
tickets = [t for t in charset_universe]
print('O' in tickets, 'I' in tickets, 'L' in tickets) # False, False, False


# Limited, generate only a part of the universe
limited_universe = Universe([RangedPosition(0, 999)])
print(len([t for t in limited_universe.generate(limit=10, offset=2])) #8
```
