import os
import sys
import string

PRINTABLE_WITHOUT_DIGITS = set(string.printable) ^ set(string.digits)


class LineInFileError(Exception): pass


class LuckyTicket:
    def __init__(self, path):
        self.path = path

    def _is_file_exists(self):
        if not os.path.isfile(self.path) and \
                not os.path.exists(self.path):
            raise FileNotFoundError('Enter correct path to the file')

    @staticmethod
    def _is_valid_line(line: str):
        is_not_valid_data = False

        for i in line:
            if i in PRINTABLE_WITHOUT_DIGITS:
                is_not_valid_data = True

        if is_not_valid_data or len(line) != 6:
            raise LineInFileError(
                'Invalid data in file: {}'.format(line)
            )

    def count_moskow_tickets(self):
        self._is_file_exists()
        file = open(self.path, encoding="utf-8")
        counter = 0

        for line in file:
            line = line.strip()
            self._is_valid_line(line)

            if sum(map(int, line[:3])) == sum(map(int, line[3:])):
                counter += 1

        return counter

    def count_piter_tickets(self):
        self._is_file_exists()
        file = open(self.path, encoding="utf-8")
        counter = 0

        for line in file:
            line = line.strip()
            self._is_valid_line(line)

            if sum(map(int, line[::2])) == sum(map(int, line[1::2])):
                counter += 1

        return counter


if __name__ == '__main__':
    if len(sys.argv) == 3:
        tickets = LuckyTicket(sys.argv[2])
        if sys.argv[1].lower() == '-m':
            print(tickets.count_moskow_tickets())
        if sys.argv[1].lower() == '-p':
            print(tickets.count_piter_tickets())

    else:
        print(
            """
            You enter wrong parameters.
            - Enter mode (-m) to count in Moskow mode
                         (-p) to count in Piter mode
                         
            - Enter valid path to your file
            """
        )
