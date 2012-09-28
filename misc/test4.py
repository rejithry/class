'''
Created on Apr 29, 2012

@author: Rejith
'''
import re
print ord('9')
print ord('0')
print ord('a')
print ord('f')

def to_dec(a):
    t = 0
    l = list(a)
    print l
    for i in l:
        he = 10 + ord(i) - ord('a')
        if he < 17 and he > 9:
            t = t * 16 + he
        else:
            t = t*16 + int(i)
    return t

print to_dec('19')
print  re.match(r'[A-Z]+','YOU').group(0) == 'YOU'
print 'hello world'[::-1]

for i in range(2,10):
    print i



