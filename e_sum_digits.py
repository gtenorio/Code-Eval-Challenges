__author__ = 'Gio'
#Code Eval: Sum of Digits
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	total = 0
	for i in test:
		if i != '\n':
			total += int(i)
	print(total)
test_cases.close()
