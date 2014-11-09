__author__ = 'Gio'
#Code Eval: Read More
import sys

def trim(s):
	if len(s) <= 55:
		print(s, end = '')
	else:
		s = s[0:40]
		q = 39
		
		while len(s) != 0:
			if s[q] == ' ':
				s = s.rstrip(' ')
				break
			else:
				s = s[:-1]
				q -= 1
		print(s, '... <Read More>', len(s), sep = '')

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	trim(test)
test_cases.close()
