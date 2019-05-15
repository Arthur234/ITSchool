
class ChessDesk:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        if str(height) in '' and str(width) in '':
            ChessDesk.get_instructions()
        elif self.verification_by_type() and self.verification_by_data():
            self.desk = self.create_desk()
            print(self.desk)

    def verification_by_type(self):
        if type(self.width) == int and type(self.height) == int:
            return True
        else:
            raise TypeError('Invalid type: {} and {}'.format(type(self.height), type(self.width)))

    def verification_by_data(self):
        if 1 < self.height < 121 or 1 < self.width < 121:
            return True
        else:
            raise ValueError('Data out of range: {} and {}'.format(self.height, self.width))

    def create_desk(self):
        symbols = ('*', ' ')
        desk = ''

        for h in range(self.height):
            for w in range(self.width):
                desk += symbols[(h + w) % 2]

            desk += '\n'
        return desk

    @staticmethod
    def get_instructions():
        return 'write instructions'


if __name__ == '__main__':
    ChessDesk(2, 2)
