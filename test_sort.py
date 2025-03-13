import unittest
from random import randint

from constants import STANDARD, SPECIAL, REJECTED, INVALID
from main import sort


class TestSort(unittest.TestCase):
    """Test scenarios for the sort method"""

    VOLUME_COMBINATIONS = [
        [150, 1, 1],
        [1, 150, 1],
        [1, 1, 150],
        [100, 100, 100],
    ]

    INVALID_VALUES = [-1, -200, 0, -1.1]

    def test_rejected(self):
        for combination in self.VOLUME_COMBINATIONS:
            stack = sort(*combination, randint(20, 1000))
            self.assertEqual(stack, REJECTED)

    def test_special_by_volume_and_dimension(self):
        for combination in self.VOLUME_COMBINATIONS:
            stack = sort(*combination, randint(0, 19))
            self.assertEqual(stack, SPECIAL)

    def test_special_by_mass(self):
        stack = sort(1, 1, 1, randint(20, 1000))
        self.assertEqual(stack, SPECIAL)

    def test_standard(self):
        stack = sort(1, 1, 1, randint(0, 19))
        self.assertEqual(stack, STANDARD)

    def test_invalid_wdith(self):
        for value in self.INVALID_VALUES:
            stack = sort(value, 0.1, 0.1, 0.1)
            self.assertEqual(stack, INVALID)

    def test_invalid_height(self):
        for value in self.INVALID_VALUES:
            stack = sort(0.1, value, 0.1, 0.1)
            self.assertEqual(stack, INVALID)

    def test_invalid_length(self):
        for value in self.INVALID_VALUES:
            stack = sort(0.1, 0.1, value, 0.1)
            self.assertEqual(stack, INVALID)

    def test_invalid_mass(self):
        for value in self.INVALID_VALUES:
            stack = sort(0.1, 0.1, 0.1, value)
            self.assertEqual(stack, INVALID)
