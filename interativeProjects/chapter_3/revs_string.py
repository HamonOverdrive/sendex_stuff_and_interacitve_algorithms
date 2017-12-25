# from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
	m = Stack()
	word = ''
	for i in mystr:
		m.push(i)
	for k in range(len(mystr)):
		word += m.pop()
	print(word)
	# return word

revstring('apple')

# testEqual(revstring('apple'),'elppa')
# testEqual(revstring('x'),'x')
# testEqual(revstring('1234567890'),'0987654321')