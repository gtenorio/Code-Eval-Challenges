__author__ = 'Gio'
#Code Eval: Hex to Decimal
import sys
import math

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	print(int(test, 16), )
test_cases.close()
