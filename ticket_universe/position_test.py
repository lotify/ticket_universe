import unittest

from ticket_universe import charsets, errors
from ticket_universe.position import (
    Position,
    AlphaPosition,
    FixedPosition,
    BinaryPosition,
    NumericPosition,
    RangedPosition,
)


class PositionTest(unittest.TestCase):
    def test_position_length_equals_character_length(self):
        chars = list("123")
        self.assertEqual(len(chars), len(Position(chars)))

    def test_position_iteration_equals_character_list(self):
        chars = list("123")
        self.assertEqual(chars, [char for char in Position(chars)])

    def test_building_position_from_string(self):
        ranged_position = Position.from_string("ranged:0:255")
        self.assertIsInstance(ranged_position, RangedPosition)
        self.assertEqual(256, len(ranged_position))

        alpha_position = Position.from_string("alpha")
        self.assertIsInstance(alpha_position, AlphaPosition)
        self.assertEqual(charsets.latin(), alpha_position.characters)

        alpha_latin_safe_position = Position.from_string("alpha:safe_latin")
        self.assertIsInstance(alpha_latin_safe_position, AlphaPosition)
        self.assertEqual(charsets.safe_latin(), alpha_latin_safe_position.characters)

        expected_fixed_value = "fixed-element-"
        fixed_position = Position.from_string("fixed:" + expected_fixed_value)
        self.assertIsInstance(fixed_position, FixedPosition)
        self.assertEqual(1, len(fixed_position))
        self.assertEqual([expected_fixed_value], fixed_position.characters)


class FixedPositionTest(unittest.TestCase):
    def test_position_length_equals_one(self):
        self.assertEqual(1, len(FixedPosition("a")))
        self.assertEqual(1, len(FixedPosition("ab")))


class RangedPositionTest(unittest.TestCase):
    def test_range_expectations_match_length(self):
        self.assertEqual(256, len(RangedPosition(0, 255)))
        self.assertEqual(0, len(RangedPosition(0, 0)))


class BinaryPositionTest(unittest.TestCase):
    def test_position_length_equals_two(self):
        self.assertEqual(2, len(BinaryPosition()))


class NumericPositionTest(unittest.TestCase):
    def test_position_length_equals_ten(self):
        self.assertEqual(10, len(NumericPosition()))


class AlphaPositionTest(unittest.TestCase):
    def test_sane_defaults_are_used(self):
        self.assertTrue(len(AlphaPosition()) > 0)

    def test_charset_can_be_specified(self):
        self.assertEqual(
            charsets.safe_latin(), [char for char in AlphaPosition("safe_latin")]
        )

    def test_invalid_charset_raises_exception(self):
        with self.assertRaises(errors.MissingCharset):
            AlphaPosition("invalid_charset")
