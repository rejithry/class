'''
Created on Mar 18, 2012

@author: Rejith
'''
import os
import re
def print_multiplication_table(n):
    i,j = 1,1
    while i <= n:
        j = 1
        while j <= n:
            print str(i) + ' * ' + str(j) + ' = ' +str(i*j)
            j = j + 1;
        i = i + 1
        
        
#print_multiplication_table(10)
s= list('Hello')
square_list = [num*num*num for num in range(1,101)]
#print square_list
s = ['mv "'+ s + '" "' + s+'.gpg"' for s in  os.listdir('c:\\Program Files')]
f = open('f:\\output.txt', 'w')
f.write("\n".join(s))
page = "http://www.google.com/blogsearch?hl=en&tab=wb"
p = re.compile('(http://|www.)')
print  re.compile('(.com.*)').sub('.com',re.compile('(http://|www.)').sub( '', page))

print re.findall(r'[\w.]+@[\w.]+','rejith.raghavan@nike.com fdfjdhjhfjdh fjdhfjh djffjdhfj  rejith.ry@gmail.com bkdlskdks')


