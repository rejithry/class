'''
Created on Apr 14, 2012

@author: Rejith  
'''

f = open('f://HashInt.txt','r')

d = {}
l = []
s = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]
for i in f:
    d[int(i.strip())] = int(i.strip())
    l.append(int(i.strip()))

for j in s:
    found = False
    for i in l:
        if j-i in d:
            found = True
            print i, j - i
            break
    print found

    