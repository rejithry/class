#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where 
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#

def bipartite(G):
    for i in G:
        v = i
        break
    q = []
    part1 = []
    part2 = []
    color = {}
    is_bipartite = True
    
    q.append(v)
    color[v] = 'b'
    part2.append(v)

    while len(q) > 0 :
        t = q.pop(0)
        for  x in G[t]:
            if  x in color and color[t] == color[x]:
                is_bipartite = False
                break
            elif x in color and color[t] != color[x]:
                continue
            else:
                if color[t] == 'r':
                    color[x] = 'b'
                    part2.append(x)
                else:
                    color[x] = 'r'
                    part1.append(x)
                q.append(x)
        if not is_bipartite:
            break

    return set(part1) if is_bipartite else None


########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None
