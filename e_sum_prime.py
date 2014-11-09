__author__ = 'Gio'
#Code Eval: Sum of 1st 1000 primes

sum = 0
count = 0
num = 2
while count < 1000:
    isPrime = True
    for j in range(2, num):
        if num % j == 0:
            isPrime = False
    if isPrime:
        sum += num
        count += 1
    num += 1
print(sum)

