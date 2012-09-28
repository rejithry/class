'''
Created on Mar 22, 2012

@author: Rejith
'''

def split_string(source,splitlist):
    t = list(source)
    sep = list(splitlist)
    target=''
    pos = 0
    for i in t:
        if i in sep:
            t[pos] = ' '
        pos = pos + 1
    
    for i in range(0,len(source)):
        target = target + t[i]
    
    return target.split()

print split_string("After  the flood   ...  all the colors came out.", " .")