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
    marked = bfs(G,i)
    if j not in marked:
        return None
    max_distance = (i,i,0)
    for k in G:
        for l in G[k]:
            if G[k][l] > max_distance[2]:
                max_distance = (l,k,G[k][l])
    print max_distance
    print dfs(G,i,max_distance[0]), i, l
    print dfs(G,max_distance[1],j),k,j
    return dfs(G,i,max_distance[0])+dfs(G,max_distance[1],j)

def bfs(G,v):
    q = []
    marked = {}
    short_path = {}
    q.append(v)
    marked[v] = 1
    short_path [v] = 0
    while len(q) > 0 :
        t = q.pop(0)
        for  x in G[t]:
            if x not in marked:
                marked[x] = 1
                short_path[x] = short_path[t] + 1
                q.append(x)
    return marked
def dfs(G, v, u):
    s = []
    path = []
    visited = {}
    s.append(v)
    while len(s) != 0:
        t = s.pop(-1)
        if t == u:
            path.append(t)
            return path
        #if len(path) > 0 and t in G[path[-1]]:
        path.append(t)
        for  x in G[t]:
            if x not in visited:
                s.append(x)
                visited[x] = 1
    return path

def shortest_path(G,v, u):
    q = []
    marked = {}
    short_path = {}
    q.append(v)
    marked[v] = 1
    short_path [v] = 0
    path=[]
    path.append(v)
    while len(q) > 0 :
        t = q.pop(0)
        if t == u:
            break
        neighbors = G[t]
        count = 0
        for  x in G[t]:
            count = count + 1
            if x not in marked:
                if x == u:
                    path.append(x)
                    return path
                marked[x] = 1
                short_path[x] = short_path[t] + 1
                q.append(x)
                path.append(x)
                if count < len(neighbors):
                    path.append(t)
    return path

#########
#
# Test

def score_of_path(G, path):
    print path
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
    print dfs(G, 'a','d')
    print dfs(G, 'd','b')
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
