import unittest

from elementary_task.Task6.lucky_tickets import LuckyTicket


class TestLuckyTicket(unittest.TestCase):
    def setUp(self) -> None:
        self.ticket = LuckyTicket('Test_data_for_tickets.txt')

    def test_count_moskow_tickets(self):
        expected = 3
        now = self.ticket.count_moskow_tickets()
        self.assertEqual(expected, now)

    def test_count_piter_tickets(self):
        expected = 3
        now = self.ticket.count_piter_tickets()
        self.assertEqual(expected, now)
