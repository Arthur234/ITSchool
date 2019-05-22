import unittest

from elementary_task.Task8.fibonacci_numbers import FibonacciNumbers


class TestFibonacci(unittest.TestCase):

    def setUp(self) -> None:
        self.fibonacci = FibonacciNumbers(0, 1234)

    def test_count_fibonacci_good_sample(self):
        expected = ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89', '144', '233', '377', '610', '987']
        now = self.fibonacci.count_fibonacci()
        self.assertEqual(expected, now)
