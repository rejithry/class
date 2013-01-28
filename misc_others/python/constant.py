#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#
paths = {}
def process_graph(G):
    for i in G:
        paths[i] = bfs(G,i)

        
        

#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(i, j):
    return True if j in paths[i]  else False

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
    return marked.keys()
#######
# Testing
#
def test():
    G = {1:{2:1},
         2:{1:1},
         3:{4:1},
         4:{3:1},
         5:{}}
    process_graph(G)
    assert is_connected(1, 2) == True
    assert is_connected(1, 3) == False

    G = {1:{2:1, 3:1},
         2:{1:1},
         3:{4:1, 1:1},
         4:{3:1},
         5:{}}
    process_graph(G)
    assert is_connected(1, 2) == True
    assert is_connected(1, 3) == True
    assert is_connected(1, 5) == False

test()
