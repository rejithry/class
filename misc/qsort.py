'''
Created on Mar 25, 2012

@author: Rejith
'''
import math
a1 = []
f = open('f:\QuickSort.txt' , 'r')

for i in f:
    a1.append(int(i.strip()))
    
#a1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
count = 0
def sort(a):
    if len(a) == 1 or len(a) == 0:
        return a
    else:
        global count
        count = count + len(a)-1
        #a[0],a[-1] = a[-1],a[0]
        piv_pos  = median(a)
        a[0],a[piv_pos] = a[piv_pos],a[0]
        piv = a[0]
        i = 1
        for j in range(1, len(a)):
            if a[j] < piv:
                a[j], a[i] = a[i],a[j]
                i = i + 1
        a[i-1],a[0] = a[0],a[i-1]
        return sort (a[:i-1]) + a[i-1:i] +  sort (a[i:])

def median(a):
    x = a[0]
    y = a[-1]
    pos = 0
    if  len(a)%2 == 0:
        z=a[len(a)/2 -1]
        pos = len(a)/2 -1
    else:
        z = a[int(len(a)/2)] 
        pos = int(len(a)/2)
     
    if x > y and x > z:
        if y > z:
            return -1 
        else :
            return pos
    elif y > z and y > x:
        if x > z:
            return 0 
        else :
            return pos
    else:
        if x > y:
            return 0 
        else :
            return -1



    
b = sort(a1)
print b
print count


    
    