__author__ = 'Gio'
#Code Eval: Remove Character
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.split(', ')
	char = test[1]
	q = test[0]
	for c in char:
		q = q.replace(c, "")
	print(q)
			
test_cases.close()
