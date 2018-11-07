# Ticket Universe
A toolset to generate a universe of unique ticket codes in Python 3.x.

## Installation
The ticket universe can be installed via pip: `pip install ticket-universe`.

## Examples
```python
from ticket_universe.position import FixedPosition, AlphaPosition, NumericPosition, RangedPosition
from ticket_universe.universe import Universe


standard_universe = Universe([
    FixedPosition('LTFY-'),
    AlphaPosition(),
    NumericPosition(),
    NumericPosition()
])

# ['ACME-A00', ..., 'ACME-Z99']
print([t for t in standard_universe])


# Alternate charsets for alpha positions
charset_universe = Universe([AlphaPosition('safe_latin'), AlphaPosition('safe_latin')])
tickets = [t for t in charset_universe]
print('O' in tickets, 'I' in tickets, 'L' in tickets) # False, False, False


# Limited, generate only a part of the universe
limited_universe = Universe([RangedPosition(0, 999)], limit=10, offset=2)
print(len([t for t in limited_universe])) #8
```
