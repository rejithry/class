# Expanding Exp
# This is very, very difficult.

import itertools

grammar = [ 
    ("a",["a1"]),
    ("a",["a2"]),
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]


def expand(tokens, grammar):
    r = {}
    for pos in range(len(tokens)):
        for rule in grammar:
            if tokens[pos] == rule[0]:
                if tokens[pos] in r:
                    r[tokens[pos]].append(rule[1])
                else:
                    r[tokens[pos]] = [rule[1]]
        if tokens[pos] not in r:
            r[tokens[pos]] = [[tokens[pos]]]
    lengths = {}  
     
    total_len = 1    
    for i in r:
        lengths[i] = len(r[i])
    for i in lengths:
        total_len = total_len * lengths[i]
    f = []
    for i in range(0,total_len):
        f.append([])
    
    for i in lengths:
        for j in range(0,total_len):
            f[j] = f[j] + r[i][j/(total_len/lengths[i])]

    for pos in range(len(tokens)):
        for rule in grammar:
            if tokens[pos] == rule[0]:
                yield tokens[0:pos] + rule[1] + tokens[pos+1:]

            
depth = 1
utterances = [["a","exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]
for sentence in utterances:
    print sentence
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']