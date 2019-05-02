from elementary_task.helper.controller import Controller


class Envelope:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        if self.check():
            self.parallel_comparison()
        elif self.a == '' and self.b == '' and self.c == '' and self.d == '':
            Controller.instruction('Enter sides of your Envelopes:\n '
                                   '1st - (a, b) \n 2nd - (c,d)')
        else:
            Controller.wrong_parameters_alert()

    def parallel_comparison(self):
        if (self.a > self.c and self.b > self.d) or (self.a > self.d
                                                     and self.b > self.c):
            print('can be invested')
        else:
            print('can\'t be invested')

    def check(self):
        if str(self.a).replace('.', '', 1).isdigit() and \
                str(self.b).replace('.', '', 1).isdigit() and \
                str(self.c).replace('.', '', 1).isdigit() and \
                str(self.d).replace('.', '', 1).isdigit():
            return True
        else:
            return False


if __name__ == '__main__':
    while True:
        a = float(input('Enter a: '))
        b = float(input('Enter b: '))
        c = float(input('Enter c: '))
        d = float(input('Enter d: '))

        Envelope(a, b, c, d)

        y = input('Are you want to continue? (y/n)  ')

        if y.lower() == 'y' or y.lower() == 'yes':
            continue
        else:
            print('Good luck')
            break
