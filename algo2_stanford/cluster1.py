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
    f = open('c:\\clustering1.txt' , 'r')

    head = 0

    g = []

    for i in f:
        if head != 0:
            s = i.strip().split(' ')
            g.append([int(s[0]), int(s[1]), int(s[2])])
        head += 1

    #print sorted(g, key = lambda a : a[2])

    mst = get_mst(sorted(g, key = lambda a : a[2]))

    print mst

def get_mst(g):
    mst = {}
    mst_u = {}

    for edge in g:
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
    return sorted(mst_l , key = lambda a : a[2], reverse =  True)

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
