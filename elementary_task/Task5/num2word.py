def generate_dict(*data, start_with=0):
    return {number: name for number, name in enumerate(data, start=start_with)}


units = generate_dict(*[
    '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь',
    'восемь', 'девять'
])

units_for_thousands = generate_dict(*[
    'тысяч', 'одна тысяча', 'две тысячи', 'три тысячи',
    'четыре тысячи', 'пять тысяч', 'шесть тысяч',
    'семь тысяч', 'восемь тысяч', 'девять тысяч'
])

units_with_tens = generate_dict(*[
    'десять', 'одиннадцать', 'двенадцать', 'тринадцать',
    'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
    'восемнадцать', 'девятнадцать'
])

units_with_tens_for_thousands = generate_dict(*[
    'десять тысяч', 'одиннадцать тысяч', 'двенадцать тысяч',
    'тринадцать тысяч', 'четырнадцать тысяч', 'пятнадцать тысяч',
    'шестнадцать тысяч', 'семнадцать тысяч', 'восемнадцать тысяч',
    'девятнадцать тысяч'
])

tens = generate_dict(*[
    '', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
    'семьдесят', 'восемьдесят', 'девяносто'
])

hundreds = generate_dict(*[
    '', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот',
    'семьсот', 'восемьсот', 'девятьсот'
])

UNITS = 0
TENS_FOR_UNITS = 1

UNITS_FOR_THOUSANDS = 3
TENS_FOR_THOUSANDS = 4

DATA = dict(
    units=units, units_for_thousands=units_for_thousands,
    units_with_tens=units_with_tens, tens=tens,
    units_with_tens_for_thousands=units_with_tens_for_thousands,
    hundreds=hundreds
)


class Num2Words:
    def __init__(self, number):
        self.number = number
        self.result = self.transform()

        print(' '.join(self.result))

    def transform(self):
        self._convert_number_to_reversed_list()
        result = []

        pattern = self._create_valid_pattern()

        for num in zip(self.number, pattern):
            result.append(DATA[num[1]][num[0]])

        return list(filter(lambda x: x != '', result))[::-1]

    def _create_valid_pattern(self):
        pattern = ['units', 'tens', 'hundreds', 'units_for_thousands', 'tens']

        if len(self.number) > 1 and self.number[TENS_FOR_UNITS] == 1:
            pattern[UNITS] = 'units_with_tens'
        if len(self.number) > 4 and self.number[TENS_FOR_THOUSANDS] == 1:
            pattern[UNITS_FOR_THOUSANDS] = 'units_with_tens_for_thousands'

        return pattern

    def _convert_number_to_reversed_list(self):
        try:
            self.number = [int(i) for i in str(self.number)[::-1]]
        except ValueError:
            raise ValueError('Invalid data')


if __name__ == '__main__':
    try:
        Num2Words('1245d')
    except ValueError:
        print('a')