import this 

class Reader:
    def __init__(self):

	s = this.s.decode('rot13')
	self.text = ' '.join(s.splitlines())

    def counter(self, word):
	return self.text.count(word)

    def to_upper(self):
        return self.text.upper()

    def replacer(self, from_symbol, to_symbol):
        return self.text.replace(from_symbol, to_symbol)

class Num:
    def __init__(self, number):
	self.number = number
    
    def mult(self):
	number = str(self.number)
	result = 1
	for i in number:
	    result *= int(i)
	return result

    def reversed(self):
	return str(self.number)[::-1]

    def sorted(self):
	sorted_number = [int(i) for i in str(self.number)]
	sorted_number.sort()
	return sorted_number

if __name__ == '__main__':

    reader = Reader()
    # 1.1
    print('better: {0}'.format(reader.counter('better')))
    print('never: {0}'.format(reader.counter('never')))
    print('is: {0}'.format(reader.counter('is')))

    # 1.2 
    print(reader.to_upper())

    # 1.3 
    print(reader.replacer('i', '$'))

#######################################################################
    num = Num(5234)
  
    # 2.1 
    print(num.mult())

    # 2.2 
    print(num.reversed())

    # 2.3 
    print(num.sorted())
#######################################################################
    a,b = 1,2
    a, b = b, a
    print(a, b)
