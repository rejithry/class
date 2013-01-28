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
def create_labels(binarytreeG, root):
    labels =  add_label(binarytreeG,root,root)
    l = {}
    for i in labels:
        if i == labels[i]['p']:
            l[i] = {i:0}
        else:
            l[i] = {i:0}
            j = labels[i]['p']
            length = binarytreeG[i][j]
            while(True):
                l[i][j] = length
                cur_j = j
                j = labels[j]['p']
                if j == cur_j:
                    break
                length += binarytreeG[cur_j][j] 
    return l

def add_label(binarytreeG, root, parent):
    labels = {}
    if len(binarytreeG[root]) == 1:
        return {root:{ 'p': parent ,'l' : None, 'r': None}}
    if len(binarytreeG[root]) == 2 and root != parent:
        for i in binarytreeG[root]:
            if i != parent:
                l = i
        return {root:{ 'p': parent ,'l' : l, 'r': None} , l:{ 'p': root ,'l' : None, 'r': None}}
    labels['p'] = parent
    count = 0
    for i in binarytreeG[root]:
        if count == 0 and i != parent:
            labels['l'] = i
            count =1
        elif count == 1 and i != parent: 
            labels['r'] = i
        else:
            continue
    x = {root : labels}
    return dict(x.items() + add_label(binarytreeG,x[root]['l'], root).items() + add_label(binarytreeG,x[root]['r'], root).items())  
        
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

def make_link(G, node1, node2, weight):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def test():
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2, 1)
    labels = create_labels(tree, 1)
    distances = get_distances(tree, labels)
        
    assert distances[1][2] == 1
    assert distances[1][4] == 2
    assert distances[1][2] == 1
    assert distances[1][4] == 2
    
    assert distances[4][1] == 2
    assert distances[1][4] == 2
    assert distances[2][1] == 1
    assert distances[1][2] == 1
    
    assert distances[1][1] == 0
    assert distances[2][2] == 0
    assert distances[9][9] == 0
    assert distances[2][3] == 2
    assert distances[12][13] == 2
    assert distances[13][8] == 6
    assert distances[11][12] == 6
    assert distances[1][12] == 3
    edges = [(1, 2 ,2), (1, 3, 2), (2, 4,3 ), (2, 5,3), (3, 6, 3), (3, 7, 3),
             (4, 8, 3), (4, 9,4), (5, 10,4), (5, 11,4), (6, 12,4), (6, 13,4), (7,14,4)]
    tree = {}
    for n1, n2, n3 in edges:
        make_link(tree, n1, n2, n3)
    labels = create_labels(tree, 1)
    distances = get_distances(tree, labels)


test()