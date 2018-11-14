import functools
import itertools
import operator

from typing import Generator

from ticket_universe.position import Position


class Universe:
    def __init__(self, positions: [Position]):
        self.positions = positions

    def __iter__(self) -> Generator[str, None, None]:
        return self.generate()

    def __len__(self) -> int:
        """ Calculates total size of the universe as a product of the size of each position """
        if len(self.positions) == 0:
            return 0
        return functools.reduce(operator.mul, map(len, self.positions))

    def generate(self, limit=None, offset=0) -> Generator[str, None, None]:
        """ Generates unique ticket codes within the universe """
        characters_product = itertools.product(
            *self.positions
        )  # cartesian product of character groups

        _limit = limit or len(self)

        for i, characters in enumerate(characters_product):
            if i < offset:
                continue
            if i >= _limit:
                return
            yield "".join(characters)
