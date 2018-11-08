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
it to stdout or file.

To generate a universe of ticket codes to standard out:

`ticket-universe fixed:ltfy- numeric numeric numeric numeric`

To write the same universe to a csv file:

`ticket-universe fixed:ltfy- numeric numeric numeric numeric > out.csv`


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
limited_universe = Universe([RangedPosition(0, 999)], limit=10, offset=2)
print(len([t for t in limited_universe])) #8
```
