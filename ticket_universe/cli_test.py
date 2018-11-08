import unittest

from argparse import Namespace
from ticket_universe import cli
from ticket_universe import position


class CliTest(unittest.TestCase):

    def test_ranged_position_arguments_parse_correctly(self):
        ranged_position = cli.position_from_arg('ranged:0:255')
        self.assertIsInstance(ranged_position, position.RangedPosition)
        self.assertEqual(256, len(ranged_position))

    def test_alpha_position_arguments_parse_correctly(self):
        alpha_position = cli.position_from_arg('alpha')
        self.assertIsInstance(alpha_position, position.AlphaPosition)
        self.assertEqual(26, len(alpha_position))

        alpha_latin_safe_position = cli.position_from_arg('alpha:safe_latin')
        self.assertIsInstance(alpha_latin_safe_position, position.AlphaPosition)
        self.assertEqual(23, len(alpha_latin_safe_position))

    def test_fixed_position_arguments_parse_correctly(self):
        fixed_position = cli.position_from_arg('fixed:fixed-element-')
        self.assertIsInstance(fixed_position, position.FixedPosition)
        self.assertEqual(1, len(fixed_position))

    def test_limiting_output(self):
        args = Namespace(positions=['binary', 'binary', 'binary'], limit=4, offset=0)
        uni = cli.universe_from_args(args)
        tickets = [t for t in uni]
        self.assertEqual(len(uni) - 4, len(tickets))

    def test_offsetting_output(self):
        args = Namespace(positions=['binary', 'binary', 'binary'], limit=None, offset=4)
        uni = cli.universe_from_args(args)
        tickets = [t for t in uni]
        self.assertEqual(len(uni) - 4, len(tickets))
