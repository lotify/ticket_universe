import unittest

from ticket_universe.position import BinaryPosition
from ticket_universe.universe import Universe


class UniverseTest(unittest.TestCase):
    def test_universe_size_equals_size_cartesian_product_size(self):
        universe = Universe([BinaryPosition(), BinaryPosition(), BinaryPosition()])
        tickets = [ticket for ticket in universe]
        self.assertEqual(
            8,
            len(tickets),
            "A binary universe with three positions should be length 2 ** 3 == 8",
        )
        self.assertEqual(
            len(universe),
            len(tickets),
            "Universe length should equal resulting ticket list length",
        )

    def test_universe_is_unique(self):
        universe = Universe([BinaryPosition(), BinaryPosition(), BinaryPosition()])
        tickets = [ticket for ticket in universe]
        self.assertEqual(8, len(set(tickets)), "The binary universe should be unique")

    def test_limited_universe(self):
        ticket_limit = 3
        universe = Universe(
            [BinaryPosition(), BinaryPosition(), BinaryPosition()], limit=ticket_limit
        )
        tickets = [ticket for ticket in universe]
        self.assertEqual(
            ticket_limit, len(tickets), "The universe should obey the ticket limit"
        )

    def test_offset_universe(self):
        offset = 2
        universe = Universe(
            [BinaryPosition(), BinaryPosition(), BinaryPosition()], offset=offset
        )
        tickets = [ticket for ticket in universe]
        self.assertEqual(6, len(tickets))

    def test_offset_limit_universe(self):
        universe = Universe(
            [BinaryPosition(), BinaryPosition(), BinaryPosition()], limit=4, offset=2
        )
        tickets = [ticket for ticket in universe]
        self.assertEqual(2, len(tickets))
