# 
# In the shortest-path oracle described in Andrew Goldberg's
# interview, each node has a label, which is a list of some other
# nodes in the network and their distance to these nodes.  These lists
# have the property that
#
#  (1) for any pair of nodes (x,y) in the network, their lists will
#  have at least one node z in common
#
#  (2) the shortest path from x to y will go through z.
# 
# Given a graph G that is a balanced binary tree, preprocess the graph to
# create such labels for each node.  Note that the size of the list in
# each label should not be larger than log n for a graph of size n.
#

#
# create_labels takes in a balanced binary tree and the root element
# and returns a dictionary, mapping each node to its label
#
# a label is a dictionary mapping another node and the distance to
# that node
#
from random  import randint
import collections
import heapq
import copy

def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    heap = []
    heapq.heappush(heap,(0,v))
    abandoned = {}
    while len(final_dist) < len(G):
        min1 = heapq.heappop(heap)
        while min1[0] in abandoned and min1[1] in abandoned[min1[0]] :
            min1 = heapq.heappop(heap)
        w = min1[1]
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]   
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    heapq.heappush(heap,(dist_so_far[x],x))
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    if dist_so_far[x] in abandoned:
                        abandoned[dist_so_far[x]].append(x)
                    else:
                        abandoned[dist_so_far[x]] = [x]
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    heapq.heappush(heap,(dist_so_far[x],x))
    return final_dist


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
    return max(short_path.values())

def is_chain(G):
    no_vertex =  len(G)
    no_edge = 0
    for i in G:
        no_edge += len(G[i])
        if len(G[i]) > 2:
            return False
    if no_vertex - 1 == no_edge/2  :
        return True
    return False

def process_chain(G):
    labels = {}
    if len(G) == 1:
        for i in G:
            labels[i]= {i : 0}
        return labels
    elif len(G) == 2:
        for i in G:
            node_1 = i
            for j in G[i]:
                node_2 = j
                weight = G[i][j]
                break
            break
        labels[node_1] ={node_2 : weight, node_1 : 0}
        labels[node_2] ={node_1 : weight, node_2 : 0}
        return labels
    else:
        mid = find_mid(G)
        L = dijkstra(G, mid)
        splits = split_graph(G,mid)
        res = apply_labels( G, L, mid) 
        for i  in range(len(splits)):
            res = join_dict(res, process_chain(splits[i]))
        return res

def join_dict(a, b):
    dest = {}
    for i in a:
        dest[i] = a[i]
    for i in b:
        if i in dest:
            dest[i].update(b[i])
        else:
            dest[i] = b[i]
    return dest
      
def split_graph(G, mid):
    G1 = {}
    G1 = copy.deepcopy(G)
    splits = []
    for i in G1[mid]:
        l = {}
        q = []
        marked = {}
        node = i
        q.append(node)
        marked[node] = 1
        del G1[node][mid]
        l[node] = G1[node]
        while len(q) > 0 :
            t = q.pop(0)
            for  x in G1[t]:
                if x not in marked:
                    marked[x] = 1
                    q.append(x)
                    l[x] = G1[x]
        splits.append(l)
    del G1[mid]
    return splits
      
    
def apply_labels(G, L, mid):
    labels = {}
    for i in G:
        labels[i] = {}
    for i in L:
        labels[i] = {mid : L[i]}
    return labels

def find_mid(G):
    for i in G:
        mid = i
        max_path = bfs(G,i)
        break
    for i in G:
        cur_path = bfs(G,i) 
        if cur_path <  max_path:
            mid = i
            max_path = cur_path
    return mid

def create_labels(G):
    return process_chain(G)

        
#######
# Testing
#

def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.iteritems():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G