'''
Created on Mar 31, 2012

@author: Rejith
'''
import re
import random

#Declaring dictionary object to hold the graph
graph = {}

#Read the file into dictionary
f = open('F:\kargerAdj.txt','r')
for i in f:
    graph[re.findall(r'\w+',i)[0]] = re.findall(r'\w+',i)[1:]

#Print initial graph
print graph

#Find the length of graph
l = range(len(graph)-2)

#Iterating length - 2 times
for i in l:
    keys =  graph.keys()
    #Find a random key from the list of keys
    a = keys[random.randrange(1,len(graph))]
    
    #If there are multiple elements in the corresponding list, find a random element
    if len(graph[a]) > 1:
        b = graph[a][random.randrange(1,len(graph[a]))]
    else:
        b = graph[a][0]
     
    #Remove the selected vertices from each other    
    graph[a] =  [value for value in graph[a] if value != b]
    graph[b] = [value for value in graph[b] if value != a]

    #Remove the second vertex from all other vertices, and add corresponding number of first vertex
    for i in graph:
        if b in graph[i]:
            graph[i] = graph[i] + [a]* graph[i].count(b)
            graph[i] = [value for value in graph[i] if value != b]
    graph[a] = graph[a] + graph[b]
    
    #Delete the second vertex from Graph
    del graph[b]
   
#Print the minimum cut    
print graph

