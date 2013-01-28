'''
Created on Apr 4, 2012

@author: Rejith
'''
import collections
import sys
import copy
class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(graph):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
  
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    graph_with_finishing_time = sys._getframe()
    if graph_with_finishing_time.f_back and graph_with_finishing_time.f_back.f_back \
        and graph_with_finishing_time.f_back.f_back.f_code == graph_with_finishing_time.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return graph(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = graph.__doc__
  return func
graph_with_finishing_time = open('F:\\scc1.txt')
graph = {}
ft = 0
s = 0
for i in graph_with_finishing_time:
    t = i.strip().split(' ')
    if t[0] in graph:
        graph[t[0]][3].append(t[1])
    else:
        graph[t[0]] = [0,0,0,[t[1]]] 
           


def dfs_ite(graph, v):
    print v
    graph[v][0] = 1
    s=[]
    for i in graph[v][3]:
        s.append([i,graph[i]])
        print s
    while len(s) > 0:
        print s
        j = s.pop()
        for k in j[1][3]:
            if graph[k][0] == 0:
                graph[k][0] = 1
                s.append([k,graph[k]])
                
    return 

def dfs_ite1(graph, v):
    print v
    s=[]
    s.append([v,graph[v]])
    while len(s) > 0:
        j = s.pop()
        print graph
        if j[1][0] == 0:
            j[1][0] = 1 
            for k in j[1][3]:
                s.append([k,graph[k]])
                
    return 

def dfs_ite2(graph, v):
    if graph[v][0] == 1:
        return
    print v
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
            print s.pop()            
    return 

def dfs(graph, v):
    print v
    if graph[v][0] == 1:
        return 
    else:
        graph[v][0] = 1
        for i in graph[v][3]:
            if graph[i][0] == 0:
                dfs(graph,i)
        global ft
        ft = ft + 1
        print "assgined ft",v,ft
        graph[v][1] = ft
        graph[v][2] = s
        return 
            
        

def rev(graph):
    t= {}
    for i in graph:
        #print 'loop4'
        for j in graph[i][3]:
            if j in t:
                t[j][3].append(i)
            else:
                t[j] = [0,0,0,[i]]
    for i in graph:
        #print 'loop5'
        if i not in t:
            t[i]=[0,0,0,[]]
    
    return t
def construct_graph(graph,reversed_graph):
    t = {}
    for i in graph:
        #print 'loop1'
        t[str(reversed_graph[i][1])] = [0,0,0,[]]
    #print t
    for i in graph:
        for j in graph[i][3]:
            #print 'in loop 2'
            t[str(reversed_graph[i][1])][3].append(str(reversed_graph[j][1]))
    for i in graph:
        #print 'loop3'
        if i not in t:
            t[i]=[0,0,0,[]]
    return t


s='0'
#print "graph", graph    
reversed_graph =  rev(graph)
#print "reversed_graph", reversed_graph

for i in reversed_graph:
    dfs(reversed_graph,i)
#print "reversed_graph", reversed_graph
graph_with_finishing_time = construct_graph(graph,reversed_graph)
#print "graph_with_finishing_time", graph_with_finishing_time
ft = 0
l = range(1,11)
#print l
for i in l:
    l[i-1] = str(i)
#print l
for j in reversed_graph(l):
    if graph_with_finishing_time[j][0] == 0:
        s = j
        dfs(graph_with_finishing_time,j)
#print "graph_with_finishing_time",graph_with_finishing_time
reversed_graph = []
for i in graph_with_finishing_time:
    reversed_graph.append(graph_with_finishing_time[i][2])
    
print collections.Counter(reversed_graph)
