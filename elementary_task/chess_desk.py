from elementary_task.helper.controller import Controller


class ChessDesk:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.desk = ''

        if str(self.height).isnumeric() and str(self.width).isnumeric():
            self.create()
        elif self.height == '' and self.width == '':
            Controller.instruction('Enter height than enter width')
        else:
            Controller.wrong_parameters_alert()

    def create(self):
        for h in range(self.height):
            if h % 2 == 1:
                self.desk += ' '

            self.desk += ' '.join('*' * self.width) + '\n'

        print(self.desk)


if __name__ == '__main__':
    ChessDesk('',  4)