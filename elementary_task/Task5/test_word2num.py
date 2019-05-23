import unittest

from elementary_task.Task5.num2word import Num2Words


class TestWord2Num(unittest.TestCase):
    def setUp(self) -> None:
        self.number_units = Num2Words(1)
        self.number_tens = Num2Words(10)
        self.number_hundreds = Num2Words(111)
        self.number_unit_thousand = Num2Words(1234)
        self.number_tens_thousand = Num2Words(14421)

    def test_transform_by_units_good_sample(self):
        expected = 'один'
        result = self.number_units.transform()
        self.assertEqual(expected, result)

    def test_transform_by_units_bad_sample(self):
        expected = 'два'
        result = self.number_units.transform()
        self.assertNotEqual(expected, result)

    def test_transform_by_tens_good_sample(self):
        expected = 'десять'
        result = self.number_tens.transform()
        self.assertEqual(expected, result)

    def test_transform_by_tens_bad_sample(self):
        expected = 'ten'
        result = self.number_tens.transform()
        self.assertNotEqual(expected, result)

    def test_transform_by_hundreds_good_sample(self):
        expected = 'сто одиннадцать'
        result = self.number_hundreds.transform()
        self.assertEqual(expected, result)

    def test_transform_by_hundreds_bad_sample(self):
        expected = 'сто двенадцать'
        result = self.number_hundreds.transform()
        self.assertNotEqual(expected, result)

    def test_transform_by_units_thousand_good_sample(self):
        expected = 'одна тысяча двести тридцать четыре'
        result = self.number_unit_thousand.transform()
        self.assertEqual(expected, result)

    def test_transform_by_units_thousand_bad_sample(self):
        expected = 'одна тысяча двести'
        result = self.number_unit_thousand.transform()
        self.assertNotEqual(expected, result)

    def test_trandform_by_tens_thousand_good_sample(self):
        expected = 'четырнадцать тысяч четыреста двадцать один'
        result = self.number_tens_thousand.transform()
        self.assertEqual(expected, result)

    def test_trandform_by_tens_thousand_bad_sample(self):
        expected = 'четырнадцать тысяч четыреста один'
        result = self.number_tens_thousand.transform()
        self.assertNotEqual(expected, result)
