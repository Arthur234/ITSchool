def generate_dict(*data, start_with=0):
    return {number: name for number, name in enumerate(data, start=start_with)}


units = generate_dict(*['', 'один', 'два', 'три', 'четыре', 'пять',
                        'шесть', 'семь', 'восемь', 'девять'])

thousand_units = generate_dict(*['тысяч', 'одна тысяча', 'две тысячи',
                                 'три тысячи', 'четыре тысячи',
                                 'пять тысяч', 'шесть тысяч',
                                 'семь тысяч', 'восемь тысяч',
                                 'девять тысяч'])

unit_tens = generate_dict(*['десять', 'одиннадцать', 'двенадцать', 'тринадцать',
                            'четырнадцать', 'пятнадцать',
                            'шестнадцать', 'семнадцать',
                            'восемнадцать', 'девятнадцать'], )

thousand_tens = generate_dict(*['десять тысяч', 'одиннадцать тысяч', 'двенадцать тысяч',
                                'тринадцать тысяч', 'четырнадцать тысяч',
                                'пятнадцать тысяч', 'шестнадцать тысяч',
                                'семнадцать тысяч', 'восемнадцать тысяч',
                                'девятнадцать тысяч'])

tens = generate_dict(*['', '', 'двадцать', 'тридцать', 'сорок',
                       'пятьдесят', 'шестьдесят', 'семьдесят',
                       'восемьдесят', 'девяносто'])

hundreds = generate_dict(*['', 'сто', 'двести', 'триста', 'четыреста',
                           'пятьсот', 'шестьсот', 'семьсот',
                           'восемьсот', 'девятьсот'])

data = dict(units=units, tens=tens, unit_tens=unit_tens,
            hundreds=hundreds, thousand_units=thousand_units,
            thousand_tens=thousand_tens)


class Num2Words:
    def __init__(self, number):
        self.number = number
        if self.is_number():
            self.number = [int(i) for i in str(number)[::-1]]

        if self.number == [0]:
            print('ноль')
        else:
            self.result = self.transform()

        print(' '.join(self.result))

    def is_number(self):
        if type(self.number) == int:
            return True
        else:
            raise TypeError('Invalid type: {}'.format(self.number))

    def transform(self):
        pattern = ['units', 'tens', 'hundreds', 'thousand_units', 'tens']
        result = []
        is_unit_extended_tens, is_thousand_extended_tens = self.is_extended_tens()

        if is_unit_extended_tens:
            pattern[0] = 'unit_tens'
        if is_thousand_extended_tens:
            pattern[3] = 'thousand_tens'

        for num in zip(self.number, pattern):
            # print(num)
            result.append(data[num[1]][num[0]])

        result = list(filter(lambda x: x != '', result))[::-1]
        return result

    def is_extended_tens(self):
        is_unit_extended_tens = False
        is_thousand_extended_tens = False

        if len(self.number) > 1 and self.number[1] == 1:
            is_unit_extended_tens = True
        if len(self.number) > 4 and self.number[4] == 1:
            is_thousand_extended_tens = True

        return is_unit_extended_tens, is_thousand_extended_tens


if __name__ == '__main__':
    Num2Words(11312)
