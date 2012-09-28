'''
Created on Apr 4, 2012

@author: Rejith
'''
import collections
       
#Function to do depth First Search
def dfs(graph, v):
    if graph[v][0] == 1:
        return
    stack=[]
    stack.append([v,graph[v]])
    graph[v][0] = 1
    while len(stack) > 0:
        j = stack[-1]
        unvisited = False
        for k in j[1][3]:
            if graph[k][0] == 0:
                unvisited = True
                graph[k][0] = 1
                stack.append([k,graph[k]])
        if not unvisited:
            t = stack.pop()
            global finishing_time
            finishing_time = finishing_time + 1
            graph[t[0]][1] = finishing_time
            graph[t[0]][2] = leader
                        
    return 
            
        
#Function to reverse the graph
def rev(graph):
    t= {}
    for i in graph:
        for j in graph[i][3]:
            if j in t:
                t[j][3].append(i)
            else:
                t[j] = [0,0,0,[i]]
    for i in graph:
        if i not in t:
            t[i]=[0,0,0,[]]
    
    return t

#Function to reconstruct the graph for second pass of DFS
def construct_graph(graph,reversed_graph):
    t = {}
    for i in graph:
        t[str(reversed_graph[i][1])] = [0,0,0,[]]
    for i in graph:
        for j in graph[i][3]:
            t[str(reversed_graph[i][1])][3].append(str(reversed_graph[j][1]))
    for i in reversed_graph:
        if i not in t:
            t[i]=[0,0,0,[]]
    return t

#Main program
#Read the file into dictionary
f = open('F:\\scc.txt')
graph = {}

for i in f:
    t = i.strip().split(' ')
    if t[0] in graph:
        graph[t[0]][3].append(t[1])
    else:
        graph[t[0]] = [0,0,0,[t[1]]] 
   
#Setting global variables
leader='0'
finishing_time = 0


#Reverse the graph   
reversed_graph =  rev(graph)

#Run first DFS and assign finishing times
for i in reversed_graph:
    dfs(reversed_graph,i)

#Construct new graph with finishing time and original directions
graph_with_finishing_time = construct_graph(graph,reversed_graph)


l = range(1,875715)


for i in l:
    l[i-1] = str(i)

#Iterate the graph in the order of finishing times and assign leaders
for j in graph_with_finishing_time(l):
    if graph_with_finishing_time[j][0] == 0:
        leader = j
        dfs(graph_with_finishing_time,j)

#Find the SCCs
finishing_times = []
for i in graph_with_finishing_time:
    finishing_times.append(graph_with_finishing_time[i][2])

#Counts 
scc = []
scc_dict = dict(collections.Counter(finishing_times))
for i in scc_dict:
    scc.append(scc_dict[i])
print sorted(scc)[-5:]


    
