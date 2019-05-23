class Triangle:
    def __init__(self, raw_data):
        self.raw_data = raw_data.replace(' ', '').split(',')
        self.name = self.raw_data[0]

    def __str__(self):
        return '[Triangle {0}]: {1} cm'.format(self.name, self.calculate_square())

    def _set_triangle_sides(self):
        try:
            self.a = float(self.raw_data[1])
            self.b = float(self.raw_data[2])
            self.c = float(self.raw_data[3])
        except ValueError:
            raise ValueError('Invalid type')

    def calculate_square(self):
        self._set_triangle_sides()
        p = (self.a + self.b + self.c) / 2
        square = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return square


if __name__ == '__main__':
    triangles = []
    while True:
        raw_data = input('Enter: <name>, <side A>, <side B>, <side C>: ')
        try:
            Triangle(raw_data).calculate_square()
            triangles.append(Triangle(raw_data))
        except ValueError:
            print('Wrong data')

        is_break = True if input('\nContinue? [y/n]: ') == 'n' else False
        if is_break:
            triangles.sort(key=lambda c: c.calculate_square(), reverse=True)
            print(f'{"Triangles":=^40}')
            for i in triangles:
                print(i)
            break
