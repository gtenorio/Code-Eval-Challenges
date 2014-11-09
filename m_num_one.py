__author__ = 'Gio'
#Code Eval: Number of ones
import sys

def bitLenCount(int_type):
	length = 0
	count = 0
	while (int_type):
		count += (int_type & 1)
		length += 1
		int_type >>= 1
	return count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = int(test.strip('\n'))
	print(bitLenCount(test))
test_cases.close()
