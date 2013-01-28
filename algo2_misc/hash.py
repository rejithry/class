'''
Created on Mar 20, 2012

@author: Rejith
'''
import urllib
import string
def hash_func(word):
    return (ord(string.upper(word[0]))-65)%26

def test_hash(word_list):
    hash_count = [0]*26;
    for i in word_list:
        hash_count[hash_func(i)] += 1
    return hash_count    
    
print test_hash(urllib.urlopen('http://sherlock-holm.es/stories/plain-text/advs.txt').read().split())
        