import os
import sys


class FileParser:
    def __init__(self, path, input_str, replace_str=''):
        self.path = path
        self.input_str = input_str
        self.replace_str = replace_str

    def _is_file_exists(self):
        if not os.path.isfile(self.path) and \
                not os.path.exists(self.path):
            raise FileNotFoundError('Enter correct path to the file')

    def find_string(self):
        self._is_file_exists()

        file = open(self.path, encoding="utf-8")
        count = 0
        for line in file:
            count += line.count(self.input_str)

        return count

    def replace_string(self):
        self._is_file_exists()

        file = open(self.path, 'r')
        file_data = file.read()
        file.close()

        new_data = file_data.replace(self.input_str, self.replace_str)

        file = open(self.path, 'w')
        file.write(new_data)
        file.close()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path = sys.argv[1]
        input_str = sys.argv[2]

        f = FileParser(path, input_str)
        print(f.find_string())

    elif len(sys.argv) == 4:
        path = sys.argv[1]
        input_str = sys.argv[2]
        replace_str = sys.argv[3]

        f = FileParser(path, input_str, replace_str)
        f.replace_string()
        print('Done')
    else:
        print(
            """
            You enter wrong parameters.
            - To count string in your file enter:
            <path_to_file> <string>
            -To replace string in file enter:
            <path_to_file> <string> <replaced_string>
            """
        )
