__author__ = 'Gio'
#Code Eval: Counting Primes
import sys
import math

def isPrime(ashton):
	p = True
	for j in range(2, int(math.sqrt(ashton))):
		if (ashton % j == 0):
			p = False
			break
	return(p)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	a = ""
	b = ""
	c = 0
	total = 0
	temp = test.split(',')
	for i in temp:
		if c == 0:
			a = int(i)
			c += 1
		else:
			c = 0
			b = int(i)
			for eric in range(a, b):
				if isPrime(eric):
					total+=1
	print(total)
test_cases.close()
