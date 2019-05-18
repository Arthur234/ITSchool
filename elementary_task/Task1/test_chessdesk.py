import unittest

from elementary_task.Task1.chessdesk import ChessDesk


class TestChessDesk(unittest.TestCase):
    """
    TODO:
    1. Name of tests functions format: <test_method_name_functionality>
    2. Write ONE function for ONE assert
    """

    def setUp(self) -> None:
        self.desk1 = ChessDesk(15, 49)

    def test_create_desk_good_sample(self):
        pass

    def test_create_desk_bad_sample(self):
        pass


if __name__ == '__main__':
    unittest.main()
