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
    
    mst = []

    len_graph = 0

    for i in f:
        if head != 0:
            count += 1
            s = ''.join(i.strip().split(' '))
            nodes.append([count, s])
        else:
            len_graph = i.strip().split(' ')[0]
        head += 1
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)) :
            d = hamming_distance(nodes[i][1],nodes[j][1])
            if d < 3:
                clique.append([nodes[i][0],nodes[j][0],d])

    
    clique =  to_dict(clique)
        
    con_comps = get_connected_comp(clique)
    
            
    print len(con_comps) + int(len_graph) - sum(con_comps)


def to_dict(l):
    mst = {}
    for edge in l:
        if edge[0] in mst:
            mst[edge[0]][edge[1]] = edge[2]
        else:
            mst[edge[0]] = {edge[1] : edge[2]}
        if edge[1] in mst:
            mst[edge[1]][edge[0]] = edge[2]
        else:
            mst[edge[1]] = {edge[0] : edge[2]}
            
    return mst
    
def get_connected_comp(clique):
    visited = {}
    con_comp_sizes = []
    no_of_nodes = 0
    for i in clique:
        if i not in visited:
            visited[i] = 1
            no_of_nodes += 1
        else:
            continue
        s = []
        s.append(i)
        while len(s) != 0:
            t = s.pop(-1)
            for  x in clique[t]:
                if x not in visited:
                    s.append(x)
                    visited[x] = 1
                    no_of_nodes += 1
        con_comp_sizes.append(no_of_nodes)
        no_of_nodes = 0
    return con_comp_sizes


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))



if __name__ == '__main__':
    main()
