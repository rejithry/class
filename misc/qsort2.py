import math

    
a1=[1,2,3,4,5,6,7,4,8,44,23,5,8,6,7,8,1,23,8,8,88,8889,990,9,10,11,99,56,12,13,14,15]
count = 0
def sort(a):
    if len(a) < 2: return a
    else:
        i = 1
        for j in range(1, len(a)):
            if a[j] < a[0]:
                a[j], a[i] = a[i],a[j]
                i += 1
        a[i-1],a[0] = a[0],a[i-1]
        return sort (a[:i-1]) + a[i-1:i] +  sort (a[i:])

b = sort(a1)
print b
print count


    
    