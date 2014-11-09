__author__ = 'Gio'
#Code Eval: Beautiful Strings
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	lib = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	test = test.lower()
	total = 0
	mult = 1
	for i in test:
		s = ord(i)
		if s >= 97 and s <= 122:
			s -= 97
			lib[s] += 1
	lib = sorted(lib)
	for j in lib:
		total += j*mult
		mult += 1 
	print(total)
test_cases.close()
