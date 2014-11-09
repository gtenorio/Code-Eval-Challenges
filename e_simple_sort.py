__author__ = 'Gio'
#Code Eval: Simple Sort
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	temp = test.split(' ')
	o = []
	for i in temp:
		if i[0] == '-':
			a = i.strip('\n')
			a = a.lstrip('-')
			a = 0 - float(a)
			o.append(a)
		else:
			a = i.strip('\n')
			a = float(a)
			o.append(a)
	o = sorted(o)
	for j in o:
		if j == o[-1]:
			print("{:.3f}".format(j), end = '', sep = '')
		else:
			print("{:.3f}".format(j), ' ', end = '', sep = '')
	print('\n', end = '', sep = '')
test_cases.close()
