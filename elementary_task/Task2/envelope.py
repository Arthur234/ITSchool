class Envelope:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        if self.parallel_comparison():
            print('You can')
        else:
            print('Impossible')

    def parallel_comparison(self):
        return (self.a > self.c and self.b > self.d) \
               or (self.a > self.d and self.b > self.c)


if __name__ == '__main__':
    while True:
        try:
            a = float(input('Enter a: '))
            b = float(input('Enter b: '))
            c = float(input('Enter c: '))
            d = float(input('Enter d: '))
        except ValueError:
            raise ValueError('Invalid type')

        Envelope(a, b, c, d)

        y = input('Are you want to continue? (y/n)  ')

        if y.lower() == 'y' or y.lower() == 'yes':
            continue
        else:
            print('Good luck')
            break
