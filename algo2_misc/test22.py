'''
Created on Jun 17, 2012

@author: Rejith
'''
import itertools
import re



def func(str1):
    return str1[-1]

print sorted(['helloC','helloB','helloD','AhelloA'],key=func)

print list(itertools.product([1,2,3],[3,4]))

           
print [r+s for r in '23456789TJQKA' for s in 'SHDC']

print re.findall('a','arejitah')

print ''.join(['a','b'])