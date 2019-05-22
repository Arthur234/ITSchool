import unittest

from elementary_task.Task7.integers_in_square import Integers


class TestIntegers(unittest.TestCase):
    def setUp(self) -> None:
        self.integers = Integers(10)

    def test_count_integers_good_sample_for_10(self):
        expected = ['1', '2', '3']
        now = self.integers.count_integers()
        self.assertEqual(expected, now)

    def test_count_integers_bad_sample_for_10(self):
        expected = [1, 2]
        now = self.integers.count_integers()
        self.assertNotEqual(expected, now)
