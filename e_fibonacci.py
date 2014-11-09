__author__ = 'Gio'
#Code Eval: Nth fibonacci
import sys

def fib(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = int(test)
	print(fib(test))
test_cases.close()
