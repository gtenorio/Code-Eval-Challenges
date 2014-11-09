__author__ = 'Gio'
#Code Eval: Multiplication Table

for i in range(1, 13):
    line = ''
    for j in range(1, 13):
        k = i*j
        line += str('{:4}'.format(k))
    print(line.lstrip())
