import unittest

from elementary_task.Task4.file_parser import FileParser


class TestFileParser(unittest.TestCase):
    def setUp(self) -> None:
        self.fp = FileParser('test_text.txt', 'Hello', 'Hi')

    def test_find_string(self):
        expected = 1
        result = self.fp.find_string()
        self.assertEqual(expected, result)

    def test_replace(self):
        self.fp.replace_string()
        file = open(self.fp.path, 'r', encoding='utf8')
        for line in file:
            expected = line.strip()

        result = 'Hi'
        self.assertEqual(expected, result)
