def to_string(text):
   philosophy = ''
   for line in text:
	philosophy += line.strip() + ' '

   return philosophy

def counter(word, text):
    print('{0}: {1}'.format(word, text.count(word)))

def mult(number):
    number = str(number)
    result = 1
    for i in number:
	result *= int(i)

    print(result)

if __name__ == '__main__':
    text = open('zen.txt', 'r')
    philosophy = to_string(text)

    # 1.1
    counter('better', philosophy)
    counter('never', philosophy)
    counter('is', philosophy)
  
    # 1.2 
    print(philosophy.upper())

    # 1.3
    print(philosophy.replace('i', '&'))
    

    number = 1234
    # 2.1
    mult(number)  # 24

    # 2.2
    print(str(number)[::-1])

    # 2.3
    sorted_number = [int(i) for i in str(number)]
    sorted_number.sort()
    print(sorted_number)

    # 3
    a, b = 1, 2
    a, b = b, a
    print(a, b) 
