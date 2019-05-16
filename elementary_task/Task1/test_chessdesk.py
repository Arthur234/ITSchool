import unittest


from elementary_task.Task1.chessdesk import ChessDesk


class TestChessDesk(unittest.TestCase):
    def setUp(self) -> None:
        self.desk1 = ChessDesk(15, 49)
        self.desk2 = ChessDesk(121, 37)
        self.desk3 = ChessDesk(1, 80)
        self.desk4 = ChessDesk(2, 2)

    def test_verification_by_type(self):
        self.assertTrue(self.desk1.verification_by_type)
        self.assertTrue(self.desk2.verification_by_type)
        self.assertTrue(self.desk3.verification_by_type)
        with self.assertRaises(TypeError):
            ChessDesk('3', 4)

    def test_verification_by_data(self):
        self.assertTrue(self.desk1.verification_by_data)
        # self.assertRaises(ValueError, self.desk2.verification_by_data())
        # self.assertRaises(ValueError, self.desk3.verification_by_data)
        # with self.assertRaises(ValueError):
            # self.desk2.verification_by_data()

    def test_create_desk(self):
        self.assertIsNotNone(self.desk1.create_desk)
        self.assertIsNotNone(self.desk2.create_desk)
        self.assertIsNotNone(self.desk3.create_desk)

        self.assertIsInstance(self.desk1.create_desk(), str)
        self.assertIsInstance(self.desk2.create_desk(), str)
        self.assertIsInstance(self.desk3.create_desk(), str)

        self.assertEqual('* \n *\n', self.desk4.desk)


if __name__ == '__main__':
    unittest.main()
