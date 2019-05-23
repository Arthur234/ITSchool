class Integers:
    def __init__(self, n):
        self.number = n

    def _convert_to_int(self):
        try:
            self.number = int(self.number)
        except ValueError:
            raise ValueError(
                'Invalid type: {}'.format(type(self.number))
            )

    def count_integers(self):
        self._convert_to_int()
        numbers = []
        max_square = int(self.number ** 0.5)
        for i in range(1, max_square + 1):
            numbers.append(str(i))

        return numbers


if __name__ == '__main__':
    while True:
        number = input('Enter number: ')

        integers = Integers(number)
        try:
            print(', '.join(integers.count_integers()))
        except ValueError:
            print('Wrong data. Enter again')

        is_break = True if input('Continue? [y/n]: ') == 'n' else False
        if is_break:
            print('Good luck! \')')
            break
