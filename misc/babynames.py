'''
Created on Mar 18, 2012

@author: Rejith
'''
import re
f = open('f:\\babynames.txt.txt' , 'r');
 #<td>106</td> <td>Kaden</td> <td>Vanessa</td>
for line in f:
    m = re.search('<td>[\d]+</td>\s*<td>(\w*)</td>\s*<td>(\w*)</td>.*', line)
    if m: 
        print m.group(1)
        print m.group(2)
    
a = 10
print a
print a + 'hello'
    

