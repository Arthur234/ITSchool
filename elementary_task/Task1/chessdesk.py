class ChessDesk:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def _verification_by_data(self):
        if self.height <= 1 or self.width <= 1:
            raise ValueError('Data out of range: {} and {}'.format(self.height, self.width))

    def _convert_to_int(self):
        try:
            self.height = int(self.height)
            self.width = int(self.width)
        except ValueError:
            raise ValueError('Invalid type: {} and {}'.format(type(self.height), type(self.width)))

    def create_desk(self):
        self._convert_to_int()
        self._verification_by_data()

        symbols = ('*', ' ')
        desk = ''

        for h in range(self.height):
            for w in range(self.width):
                desk += symbols[(h + w) % 2]
            desk += '\n'
        return desk


if __name__ == '__main__':

    while True:

        height = input('Enter height: ')
        width = input('Enter width: ')

        desk = ChessDesk(height, width)
        try:
            print(desk.create_desk())
        except ValueError:
            print('Wrong data. Enter again')

        is_break = True if input('\nContinue? [y/n]: ') == 'n' else False
        if is_break:
            print('Good luck! \')')
            break
