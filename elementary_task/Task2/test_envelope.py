import unittest

from elementary_task.Task2.envelope import CompareEnvelopes


class TestEnvelope(unittest.TestCase):

    def setUp(self) -> None:
        self.envelopes1 = CompareEnvelopes(3, 3, 2, 2)
        self.envelopes2 = CompareEnvelopes(2, 2, 3, 3)

    def test_parallel_comparison_good_sample(self):
        expected = 'You can invest'
        now = self.envelopes1.parallel_comparison()
        self.assertEqual(expected, now)

    def test_parallel_comparison_bad_sample(self):
        expected = 'Impossible!'
        now = self.envelopes2.parallel_comparison()
        self.assertEqual(expected, now)
