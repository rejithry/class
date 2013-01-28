#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RRAGHA
#
# Created:     29/12/2012
# Copyright:   (c) RRAGHA 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    f = open('//home/rejith//Downloads//clustering3.txt' , 'r')

    head = 0
    count = 0
    nodes = []

    clique = []

    g = []

    for i in f:
        if head != 0:
            count += 1
            s = ''.join(i.strip().split(' '))
            nodes.append([count, s])
        head += 1
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)) :
            clique.append([nodes[i][0],nodes[j][0],hamming_distance(nodes[i][1],nodes[j][1])])

    #print sorted(g, key = lambda a : a[2])

    mst = get_mst(sorted(clique, key = lambda a : a[2]))

    no_of_clusters = 1

    for i in mst:
        if i[2] > 2:
            no_of_clusters += 1



    print no_of_clusters


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def get_mst(g):
    mst = {}
    mst_u = {}
    c = 1

    for edge in g:
        c += 1
        print c
        if not is_chain_edge(edge, mst):
            if edge[0] in mst_u:
                mst_u[edge[0]][edge[1]] = edge[2]
            else:
                mst_u[edge[0]] = {edge[1] : edge[2]}
            if edge[0] in mst:
                mst[edge[0]][edge[1]] = edge[2]
            else:
                mst[edge[0]] = {edge[1] : edge[2]}
            if edge[1] in mst:
                mst[edge[1]][edge[0]] = edge[2]
            else:
                mst[edge[1]] = {edge[0] : edge[2]}
    mst_l = []
    for i in mst_u:
        for j in mst_u[i]:
            mst_l.append([i,j,mst_u[i][j]])
    return sorted(mst_l , key = lambda a : a[2])

def is_chain_edge(edge, mst):
    if edge[0] in mst:
        return dfs(mst, edge[0], edge[1])
    else:
         return False

def dfs(G, v, u):
    s = []
    visited = {}
    s.append(v)
    while len(s) != 0:
        t = s.pop(-1)
        if t == u:
            return True
        for  x in G[t]:
            if x not in visited:
                s.append(x)
                visited[x] = 1
    return False


if __name__ == '__main__':
    main()
