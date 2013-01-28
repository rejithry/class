#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#

def feel_the_love(G, i, j):
    # return a path (a list of nodes) between `i` and `j`,
    # with `i` as the first node and `j` as the last node,
    # or None if no path exists
    marked, cur_path = bfs(G,i)
    if j not in marked:
        return None
    max_distance = (i,i,0)
    for k in G:
        for l in G[k]:
            if G[k][l] > max_distance[2]:
                max_distance = (l,k,G[k][l])
    m1, path_a = bfs(G,i)
    m2, path_b = bfs(G,max_distance[1])
    return path_a[max_distance[0]] + path_b[j]

def bfs(G,v):
    q = []
    marked = {}
    short_path = {}
    q.append(v)
    marked[v] = 1
    short_path [v] = 0
    paths = {}
    paths[v]=[v]
    cur_path= {}
    cur_path[v] =[v]
    while len(q) > 0 :
        t = q.pop(0)
        for  x in G[t]:
            if x not in marked:
                marked[x] = 1
                short_path[x] = short_path[t] + 1
                cur_path[x] = cur_path[t] + [x]
                q.append(x)
    return marked, cur_path

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love

def test():
    G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None
    
test()
G2= {'a':{'c':1},
     'b':{'c':1},
     'c':{'a':1, 'b':1, 'e':1, 'd':1},
     'e':{'c':1, 'd':2},
     'd':{'e':2, 'c':1, 'g':1},
     'f':{},
     'g':{'d':1, 'h':5},
     'h':{'g':5}}
path = feel_the_love(G2, 'a', 'b')
assert score_of_path(G2, path) == 5    

G3 = {'a':{'b':1,'c':2},'b':{'a':1,'c':3},'c':{'a':2,'b':3,'d':1},'d':{'c':1,'e':4,'f':5},'e':{'d':4,'f':100},'f':{'e':100,'d':5}}
path = feel_the_love(G3, 'a', 'b')
assert score_of_path(G3, path) == 100
path = feel_the_love(G3, 'a', 'e')
assert score_of_path(G3, path) == 100

G4 ={'a': {'b': 9.0199999999999996, 'e': 0.01, 'd': 0.32000000000000001, 'g': 5.7800000000000002, 'f': 6.9299999999999997, 'i': 7.6799999999999997, 'h': 5.7199999999999998, 'k': 0.26000000000000001}, 'c': {'b': 4.7699999999999996, 'e': 3.2599999999999998, 'd': 8.3800000000000008, 'i': 4.6500000000000004, 'h': 8.8599999999999994, 'k': 1.6599999999999999}, 'b': {'a': 9.0199999999999996, 'c': 4.7699999999999996, 'e': 4.1100000000000003, 'g': 8.2599999999999998, 'f': 2.23, 'i': 0.33000000000000002, 'h': 8.4399999999999995, 'k': 5.3499999999999996, 'j': 2.1299999999999999}, 'e': {'a': 0.01, 'c': 3.2599999999999998, 'b': 4.1100000000000003, 'd': 7.7400000000000002, 'f': 7.7000000000000002, 'j': 8.1600000000000001}, 'd': {'a': 0.32000000000000001, 'h': 1.01, 'c': 8.3800000000000008, 'e': 7.7400000000000002, 'f': 1.45}, 'g': {'a': 5.7800000000000002, 'h': 4.9900000000000002, 'b': 8.2599999999999998, 'i': 1.21}, 'f': {'a': 6.9299999999999997, 'b': 2.23, 'e': 7.7000000000000002, 'd': 1.45, 'i': 2.3799999999999999, 'h': 1.26, 'j': 2.0299999999999998}, 'i': {'a': 7.6799999999999997, 'c': 4.6500000000000004, 'b': 0.33000000000000002, 'g': 1.21, 'f': 2.3799999999999999, 'h': 3.8500000000000001, 'k': 6.0999999999999996}, 'h': {'a': 5.7199999999999998, 'c': 8.8599999999999994, 'b': 8.4399999999999995, 'd': 1.01, 'g': 4.9900000000000002, 'f': 1.26, 'i': 3.8500000000000001, 'k': 7.7699999999999996, 'j': 8.6899999999999995}, 'k': {'a': 0.26000000000000001, 'c': 1.6599999999999999, 'b': 5.3499999999999996, 'i': 6.0999999999999996, 'h': 7.7699999999999996, 'j': 1.22}, 'j': {'h': 8.6899999999999995, 'k': 1.22, 'b': 2.1299999999999999, 'e': 8.1600000000000001, 'f': 2.0299999999999998}}
path = feel_the_love(G4, 'a', 'c')
score_of_path(G4, path) 
