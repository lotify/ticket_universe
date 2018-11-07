# Ticket Universe
A toolset to generate a universe of unique ticket codes.

## Installation
The ticket universe can be installed via pip: `pip install ticket-universe'

## Examples
```python
from ticket_universe.position import FixedPosition, AlphaPosition, NumericPosition, RangedPosition
from ticket_universe.universe import Universe


standard_universe = Universe([
    FixedPosition('ACME-'),
    AlphaPosition(),
    NumericPosition(),
    NumericPosition()
])
# ['ACME-A00-18', ..., 'ACME-Z99-18']
print([t for t in standard_universe])


# No confusing alpha's please
charset_universe = Universe([
    AlphaPosition('safe_latin'),
    AlphaPosition('safe_latin')
])
tickets = [t for t in charset_universe]
# False, False, False
print('O' in tickets, 'I' in tickets, 'L' in tickets)


# Limited, generate only a part of the universe
limited_universe = Universe([
    RangedPosition(0, 999),
    RangedPosition(0, 999)
], limit=10, offset=2)
print(len([t for t in limited_universe])) #8
```