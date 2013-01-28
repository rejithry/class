'''
Created on Apr 4, 2012

@author: Rejith
'''
import collections

ft_map = {}
#Procedure to find the DFS of a graph starting from vertex, v, assign finishing times and leaders.
def dfs(graph, v):
    if graph[v][0] == 1:
        return
    s=[]
    s.append([v,graph[v]])
    graph[v][0] = 1
    while len(s) > 0:
        j = s[-1]
        unvisited = False
        for k in j[1][3]:
            if graph[k][0] == 0:
                unvisited = True
                graph[k][0] = 1
                s.append([k,graph[k]])
        if not unvisited:
            t = s.pop()
            global ft
            ft = ft + 1
            graph[t[0]][1] = ft
            ft_map[ft] = t[0]
            graph[t[0]][2] = leader
                        
    return 
            
        
#Procedure to reverse a graph
def rev(graph):
    #Dictionary to hold the reversed graph
    t= {}
    #Loop thru the original graph and reverse the directions.
    for i in graph:
        for j in graph[i][3]:
            if j in t:
                t[j][3].append(i)
            else:
                t[j] = [0,0,0,[i]]
    #Add any vertices, which don't have outgoing edges.
    for i in graph:
        if i not in t:
            t[i]=[0,0,0,[]]
    
    return t

#Procedure to construct a graph from finishing time and original graph directions
def construct_graph(graph,reversed_graph):
    #Dictionary to hold the return value
    t = {}
    for i in graph:
        t[str(reversed_graph[i][1])] = [0,0,0,[]]
    for i in graph:
        for j in graph[i][3]:
            t[str(reversed_graph[i][1])][3].append(str(reversed_graph[j][1]))
            
    #Add any vertices, which don't have outgoing edges.
    for i in reversed_graph:
        if i not in t:
            t[i]=[0,0,0,[]]
    return t

def is_solvable(scc_l, vert_map, rev_map):

    for i in scc_l:
        for j in scc_l[i]:
            if str(rev_map[vert_map[int(j)]*-1]) in  scc_l[i]:
                    print i,scc_l[i]
                    print j
                    print vert_map[int(j)]
                    print vert_map[int(j)]*-1
                    print rev_map[vert_map[int(j)]*-1]
                    return False
            
    return True
    

#Create graph file
a = open('e:\\2sat6.txt')
b = open('e:\\2sat1_g.txt' , 'w')

vert_map = {}
rev_map = {}

head = 0
counter = 1
s = []
for i in a:
    if head != 0:
        if int(i.strip().split(' ')[0]) not in rev_map:
            vert_map[counter] = int(i.strip().split(' ')[0])
            rev_map[int(i.strip().split(' ')[0])] = counter
            v1 = counter
            counter += 1
        else:
            v1 = rev_map[int(i.strip().split(' ')[0])]
            
        if int(i.strip().split(' ')[0])* -1 not in rev_map:
            vert_map[counter] = int(i.strip().split(' ')[0])*-1
            rev_map[int(i.strip().split(' ')[0]) * -1 ] = counter
            v2 = counter
            counter += 1
        else:
            v2 = rev_map[int(i.strip().split(' ')[0]) * -1]
            
        if int(i.strip().split(' ')[1]) not in rev_map:
            vert_map[counter] = int(i.strip().split(' ')[1])
            rev_map[int(i.strip().split(' ')[1])] = counter
            u1 = counter
            counter += 1
        else:
            u1 = rev_map[int(i.strip().split(' ')[1])]
            
        if int(i.strip().split(' ')[1])* -1 not in rev_map:
            vert_map[counter] = int(i.strip().split(' ')[1])*-1
            rev_map[int(i.strip().split(' ')[1]) * -1] = counter
            u2 = counter
            counter += 1
        else:
            u2 = rev_map[int(i.strip().split(' ')[1]) * -1]    
            
        b.write( str(u2) + ' ' + str(v1) + '\n')
        b.write( str(v2) + ' ' + str(u1) + '\n')
    head += 1
b.close()

#Read the file into dictionary
graph_with_finishing_time = open('E:\\2sat1_g.txt')
graph = {}

for i in graph_with_finishing_time:
    t = i.strip().split(' ')
    if t[0] in graph:
        graph[t[0]][3].append(t[1])
    else:
        graph[t[0]] = [0,0,0,[t[1]]] 



#Setting global variables
leader='0'
ft = 0

#Reverse the graph   
reversed_graph =  rev(graph)

#Run first DFS and assign finishing times
for i in reversed_graph:
    dfs(reversed_graph,i)
    

#Construct new graph with finishing time and original directions
graph_with_finishing_time = construct_graph(graph,reversed_graph)


l = range(1,len(vert_map) + 1)

for i in l:
    l[i-1] = str(i)

#Iterate the graph in the order of finishing times and assign leaders
for j in reversed(l):
    if graph_with_finishing_time[j][0] == 0:
        leader = j
        dfs(graph_with_finishing_time,j)

#Find the SCCs
r_graph = []
for i in graph_with_finishing_time:
    r_graph.append(graph_with_finishing_time[i][2])


scc_l = {}

#Find sccs
for i in graph_with_finishing_time: 
    if graph_with_finishing_time[i][2] in scc_l:
        scc_l[graph_with_finishing_time[i][2]].append(ft_map[int(i)])
    else:
        scc_l[graph_with_finishing_time[i][2]] = [ft_map[int(i)]]
 

solvable =  is_solvable(scc_l,vert_map, rev_map)

print solvable 






    
