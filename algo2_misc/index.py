'''
Created on Mar 19, 2012

@author: Rejith
'''

def add_to_index(index,keyword,url):
    for i in index:
        if i[0] == keyword:
            if url not in i[1]:
                i[1].append(url)
                return
    index.append([keyword,[url]])
    return
        
    
index = []

add_to_index(index,'udacity','www.udacity.com')
print index

add_to_index(index,'google','www.google.com')
print index

add_to_index(index,'udacity','www.google.com')
print index

add_to_index(index,'udacity','www.udacity.com')
print index

