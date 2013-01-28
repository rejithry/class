'''
Created on Apr 12, 2012

@author: Rejith
'''

import sys

print sys.getrecursionlimit()
sys.setrecursionlimit(1000000)
print sys.getrecursionlimit()
print range(1,10)