import unittest
from num2words import num2words

from elementary_task.Task5.num2word import Num2Words


class TestWord2Num(unittest.TestCase):
    def setUp(self) -> None:
        self.number1 = Num2Words(1234)

    def test_correct_data(self):
        for i in range(1, 100000):
            self.assertEqual(num2words(i, lang='ru'), ' '.join(Num2Words(i).result))
