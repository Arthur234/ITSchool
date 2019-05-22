class CompareEnvelopes:
    def __init__(self, a1, b1, a2, b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2

    def _convert_to_float(self):
        try:
            self.a1 = float(self.a1)
            self.b1 = float(self.b1)
            self.a2 = float(self.a2)
            self.b2 = float(self.b2)
        except ValueError:
            raise ValueError('Invalid type: {} ,{}, {} and {}'.format(
                type(self.a1), type(self.b1), type(self.a2), type(self.b2))
            )

    def parallel_comparison(self):
        self._convert_to_float()
        if (self.a1 > self.a2 and self.b1 > self.b2) \
                or (self.a1 > self.b2 and self.a2 > self.b1):
            return 'You can invest'
        else:
            return 'Impossible!'


if __name__ == '__main__':
    while True:
        a1 = input('Enter first side of the outer envelope: ')
        b1 = input('Enter second side of the outer envelope: ')
        a2 = input('Enter first side of the inner envelope:: ')
        b2 = input('Enter second side of the inner envelope:: ')

        envelopes = CompareEnvelopes(a1, b1, a2, b2)
        print(envelopes.parallel_comparison())

        is_break = True if input('\nContinue? [y/n]: ') == 'n' else False
        if is_break:
            print('Good luck! \')')
            break
