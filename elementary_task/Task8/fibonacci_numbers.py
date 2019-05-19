class FibonacciNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def _convert_to_int(self):
        try:
            self.start = int(self.start)
            self.end = int(self.end)
        except ValueError:
            raise ValueError(
                'Invalid type: {} and {}'.format(self.start, self.end)
            )

    def count_fibonacci(self):
        self._convert_to_int()
        f1, f2 = 0, 1
        result = []
        if self.start == 0:
            result.append(0, 1)

        while True:
            f1, f2 = f2, f1 + f2

            if f2 > self.start:
                result.append(f2)

            if f2 > self.end:
                break

        result.pop()
        return result


if __name__ == '__main__':
    while True:
        start = input('Start of the interval: ')
        end = input('End of the interval: ')

        fibonacci = FibonacciNumbers(start, end)
        print(*fibonacci.count_fibonacci())

        is_break = True if input('\nContinue? [y/n]: ') == 'n' else False
        if is_break:
            print('Good luck! \')')
            break
