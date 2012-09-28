'''
Created on Apr 4, 2012

@author: Rejith
'''
import collections
       
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

#Read the file into dictionary
graph_with_finishing_time = open('F:\\scc.txt')
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


l = range(1,875715)
#l = range(1,15)

for i in l:
    l[i-1] = str(i)

#Iterate the graph in the order of finishing times and assign leaders
for j in reversed(l):
    if graph_with_finishing_time[j][0] == 0:
        leader = j
        dfs(graph_with_finishing_time,j)

#Find the SCCs
reversed_graph = []
for i in graph_with_finishing_time:
    reversed_graph.append(graph_with_finishing_time[i][2])

#Counts 
scc = []
scc_dict = dict(collections.Counter(reversed_graph))
for i in scc_dict:
    scc.append(scc_dict[i])
print sorted(scc)[-5:]


    
