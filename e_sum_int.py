__author__ = 'Gio'
#Code Eval: Sum of integers from file
import sys

test_cases = open(sys.argv[1], 'r')
count = 0
for test in test_cases:
	count += int(test.strip('\n'))
test_cases.close()
print(count)
