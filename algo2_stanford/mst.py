#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RRAGHA
#
# Created:     28/12/2012
# Copyright:   (c) RRAGHA 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    f = open('c:\\edges.txt' , 'r')

    head = 0

    edges = []
    vertices = {}

    msp = []
    frontier = []
    added_vertex = []

    for i in f:
        if head != 0:
            s = i.strip().split(' ')
            edges.append([int(s[0]), int(s[1]), int(s[2])])
        head += 1
    edges.sort(key = lambda x: x[0])

    for i in edges:
        if i[0] in vertices:
            vertices[i[0]][i[1]] = i[2]
        else:
            vertices[i[0]] = {i[1] : i[2]}

        if i[1] in vertices:
            vertices[i[1]][i[0]] = i[2]
        else:
            vertices[i[1]] = {i[0] : i[2]}


    #for i in vertices:
        #print i, vertices[i]


    while(len(added_vertex) != len(vertices)):
        if len(added_vertex) == 0:
            added_vertex.append(edges[0][0])
            frontier.append(edges[0][0])
        start_ver, next_ver , weight = get_min_vertex(frontier, vertices,msp,added_vertex)
        added_vertex.append(next_ver)
        frontier.append(next_ver)
        for i in msp:
            if start_ver == i[0] or start_ver == i[1]:
                frontier.remove(start_ver)
                break
        msp.append([start_ver, next_ver , weight])

    span_distance = 0

    for i in msp:
        print i

    for i in msp:
        span_distance += i[2]
    print span_distance

def get_min_vertex(frontier, vertices, msp,added_vertex):
    edge_list = []
    for i in frontier:
        for j in vertices[i]:
            edge =  [i,j,vertices[i][j]]
            if not in_msp(edge, msp,added_vertex):
                edge_list.append(edge)
    edge_list.sort(key = lambda a: a[2])
    return edge_list[0]

def in_msp(edge, msp,added_vertex):
    for i in msp:
        if edge[1] in added_vertex:
            return True
        if (i[0] == edge[0] and i[1] == edge[1] and i[2] == edge[2]):
            return True
        if (i[1] == edge[0] and i[0] == edge[1] and i[2] == edge[2]):
            return True
    return False



if __name__ == '__main__':
    main()
