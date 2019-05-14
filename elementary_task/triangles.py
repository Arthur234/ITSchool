class Triangle:
    def __init__(self, raw_data):

        if raw_data in '':
            Triangle.get_instructions()
        else:
            self.raw_data = raw_data.replace(' ', '').split(',')
            self.name = self.raw_data[0]

            try:
                self.a = float(self.raw_data[1])
                self.b = float(self.raw_data[2])
                self.c = float(self.raw_data[3])
                self.square = self.calculate_square()
            except ValueError as err:
                print(err)
                print('Please check your data, you enter wrong parameters')

    def __str__(self):
        return '[Triangle {0}]: {1} cm'.format(self.name, self.square)

    def calculate_square(self):
        p = (self.a + self.b + self.c) / 2
        square = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return square

    @classmethod
    def get_instructions(cls):
        pass


if __name__ == '__main__':

    triangles = []
    while True:
        raw_data = input('Enter: <name>, <side A>, <side B>, <side C> ')
        triangles.append(Triangle(raw_data))
        y = input('Add more? (y/n)')

        if y == 'n':
            break

    triangles.sort(key=lambda c: c.square, reverse=True)

    for i in triangles:
        print(i)
