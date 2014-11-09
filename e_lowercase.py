__author__ = 'Gio'
#Code Eval: Lowercase
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	print(test.lower())
test_cases.close()
