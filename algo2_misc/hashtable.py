'''
Created on Mar 21, 2012

@author: Rejith
'''
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    add = 0
    for i in bucket:
        if i[0] == key :
            i[1] = value
            add = 1
            break
    if add == 0:
        bucket.append([key,value])
        
    
    

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])    


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

h = make_hashtable(5)
print h
print hashtable_get_bucket(h, 'key')

hashtable_update(h,'key','value')
hashtable_update(h,'key','value1')
hashtable_update(h,'key1','value1')
print h
