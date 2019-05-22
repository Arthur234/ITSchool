import unittest

from elementary_task.Task1.chessdesk import ChessDesk


class TestChessDesk(unittest.TestCase):

    def setUp(self) -> None:
        self.desk1 = ChessDesk(3, 2)
        self.desk2 = ChessDesk('k', 2)

    def test_create_desk_good_sample(self):
        expected = '* \n *\n* \n'
        now = self.desk1.create_desk()
        self.assertEqual(expected, now)

    def test_create_desk_bad_sample(self):
        expected = '* \n *\n* * \n'
        now = self.desk1.create_desk()
        self.assertNotEqual(expected, now)


if __name__ == '__main__':
    unittest.main()
