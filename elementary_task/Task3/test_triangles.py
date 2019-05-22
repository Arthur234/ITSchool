import unittest

from elementary_task.Task3.triangles import Triangle


class TestTriangles(unittest.TestCase):

    def setUp(self) -> None:
        self.triangle1 = Triangle('first, 3, 3, 5')
        self.triangle2 = Triangle('second, 1, 2, 5')

    def test_calculate_square_good_sample(self):
        expected = 4.14578098794425
        now = self.triangle1.calculate_square()
        self.assertEqual(expected, now)

    def test_calculate_square_bad_sample(self):
        expected = 1234
        now = self.triangle2.calculate_square()
        self.assertNotEqual(expected, now)
