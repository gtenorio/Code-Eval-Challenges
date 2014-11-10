__author__ = 'Gio'
#Code Eval: Hidden Digits
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	count = 0
	for i in range(0, len(test)):
		if(test[i] == 'a' or test[i] == '0'):
			print(0, end = '')
			count += 1
		elif(test[i] == 'b' or test[i] == '1'):
			print(1, end = '')
			count += 1
		elif(test[i] == 'c' or test[i] == '2'):
			print(2, end = '')
			count += 1		
		elif(test[i] == 'd' or test[i] == '3'):
			print(3, end = '')
			count += 1
		elif(test[i] == 'e' or test[i] == '4'):
			print(4, end = '')
			count += 1
		elif(test[i] == 'f' or test[i] == '5'):
			print(5, end = '')
			count += 1
		elif(test[i] == 'g' or test[i] == '6'):
			print(6, end = '')
			count += 1
		elif(test[i] == 'h' or test[i] == '7'):
			print(7, end = '')
			count += 1		
		elif(test[i] == 'i' or test[i] == '8'):
			print(8, end = '')
			count += 1			
		elif(test[i] == 'j' or test[i] == '9'):
			print(9, end = '')
			count += 1
		else:
			continue
	#end for
	if(count == 0):
		print("NONE")
	else:
		print()
test_cases.close()
