import itertools, operator

comic_book = open('//home//rejith//Downloads//file' , 'r')


def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node

def dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    hop_dist = {}
    hop_dist[v] = 0
    while len(final_dist) < len(G) and len(dist_so_far) != 0:
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    hop_dist[x] = hop_dist[w] + 1
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    hop_dist[x] = hop_dist[w] + 1
    return final_dist

def make_link(G, node1, node2):
    #if node1 not in G:
     #   G[node1] = {}
    #(G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def make_weighted_link(G, node1, node2, weight):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G
def make_link1(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G

G = {}
G1 = {}
pairs = {}

for i in comic_book:
    make_link(G, i.split('\t')[0].strip() , i.split('\t')[1].strip())
count = 0

pairs2 = {}

for j in G:
    for i in  itertools.combinations(G[j].keys(),2):
        if i in pairs:
            pairs[i] +=1 
        else:
            pairs[i] = 1
        if (i[1],i[0]) in pairs:
            pairs[(i[1],i[0])] +=1
        else:
            pairs[(i[1],i[0])]  = 1

for i in pairs:
    j = tuple(sorted(i))
    pairs2[j] = pairs[i]



    
for i in pairs2:
    make_link1(G1,i[0],i[1] , pairs2[i] )


for i in pairs:
    i[0]

count = 0
for i in G1:
     dijkstra(G1,i)
     print i




