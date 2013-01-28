'''
Created on Jan 20, 2013

@author: Rejith
'''

import math

def main():
    f = open('e:\\tsp.txt' , 'r')
    
    d = []
    l = 0
    coord = []
    head = 0
    
    for i in f:
        if head != 0:
            coord.append( ( float(i.strip().split(' ')[0]), float(i.strip().split(' ')[1]) ) )
        else:
            l = int(i.strip())
        head += 1
    for i in range(l):
        d.append([])
        for j in range(l):
            if i == j:
                d[i].append(0)
            else:
                x1 = coord[i][0]
                x2 = coord[j][0]
                y1 = coord[i][1]
                y2 = coord[j][1]
                
                t = ((x2 - x1)* (x2 - x1)) + ((y2 - y1)* (y2 - y1)) 
                d[i].append(math.sqrt(t))

    print (len(d))
    print (tour_len ((1,2,5,4,3,7,9,13,14,16,24,25,20,17,21,23,22,18,19,15,12,11,10,8,6), d)) 

def tour_len(t, d):
    assert len(t) == len(d) - 1
    return d[0][t[0]] + sum(d[t[i]][t[i+1]] for i in range(len(t) - 1)) +\
           d[t[-1]][0]
            
def tsp_dp_solve(d):
    def memoize(f):
        memo_dict = {}
        def memo_func(*args):
            if args not in memo_dict:
                memo_dict[args] = f(*args)
            return memo_dict[args]
        memo_func.clear = lambda: memo_dict.clear()
        return memo_func

    @memoize
    def rec_tsp_solve(c, ts):
        assert c not in ts
        if ts:
            return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
                       for lc in ts)
        else:
            return (d[0][c], 0)

    best_tour = []
    c = 0
    cs = frozenset(range(1, len(d)))
    while True:
        l, lc = rec_tsp_solve(c, cs)
        if lc == 0:
            break
        best_tour.append(lc)
        c = lc
        cs = cs - frozenset([lc])

    best_tour = tuple(reversed(best_tour))

    return best_tour
 
def tsp_rec_solve(d):
    def rec_tsp_solve(c, ts):
        assert c not in ts
        if ts:
            return min((d[lc][c] + rec_tsp_solve(lc, ts - set([lc]))[0], lc)
                       for lc in ts)
        else:
            return (d[0][c], 0)

    best_tour = []
    c = 0
    cs = set(range(1, len(d)))
    while True:
        l, lc = rec_tsp_solve(c, cs)
        if lc == 0:
            break
        best_tour.append(lc)
        c = lc
        cs = cs - set([lc])

    best_tour = tuple(reversed(best_tour))

    return best_tour       
if __name__ == "__main__":
    main()