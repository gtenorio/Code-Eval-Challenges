__author__ = 'Gio'
#Code Eval: Delta Time
import sys
test_cases = open(sys.argv[1], 'r').read().splitlines()
count = 0
h3 = 0
m3 = 0
s3 = 0
a = True
for test in test_cases:
    temp = test.split(' ')
    for i in temp:
        temp2 = i.split(':')
        for j in temp2:
            if j != '':
                k = int(j)
                if count == 0:
                    h1 = k
                    count += 1
                elif count == 1:
                    m1 = k
                    count += 1
                elif count == 2:
                    s1 = k
                    count += 1
                elif count == 3:
                    h2 = k
                    count += 1
                elif count == 4:
                    m2 = k
                    count += 1
                else:
                    s2 = k
                    count = 0
                    if h1 > h2:
                        if s1 > s2:
                            s3 = s1 - s2
                        elif s1 == s2:
                            s3 = 0
                        else:
                            s3 = (s1 + 60) - s2
                            m1 -= 1
                        if m1 > m2:
                            m3 = m1 - m2
                        elif m1 == m2:
                            m3 = 0
                        else:
                            m3 = (m1 + 60) - m2
                            h1 -= 1
                        h3 = h1 - h2
                    else:
                        if s2 > s1:
                            s3 = s2 - s1
                        elif s2 == s1:
                            s3 = 0
                        else:
                            s3 = (s2 + 60) - s1
                            m2 -= 1
                        if m2 > m1:
                            m3 = m2 - m1
                        elif m2 == m1:
                            m3 = 0
                        else:
                            m3 = (m2 + 60) - m1
                            h2 -= 1
                        h3 = h2 - h1
    #print result
    if a == True:
        if h3 > 9:
            print(h3,':', end = '', sep = '')
        else:
            print('0',h3,':', end = '', sep = '')
        if m3 > 9:
           print(m3,':', end = '', sep = '')
        else:
            print('0',m3,':', end = '', sep = '')
        if s3 > 9:
            print(s3, sep = '')
        else:
            print('0',s3, sep = '')
        a = False
    else:
        a = True

test_cases.close()