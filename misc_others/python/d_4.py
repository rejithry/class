from collections import deque
from random import  randint
def update(PQ,QPos,nodeID,value):
    pos = QPos[nodeID]
    PQ[pos][1] = value
    downHeapify(PQ,QPos,pos)
    return
def upHeapify(PQ,QPos,cp):
    cv = PQ[cp][1] #child's value = value at child's position in PQ
    while cp!=0:
        pp = int((cp-1)*0.5)
        pv = PQ[pp][1]
        if pv > cv:
            PQ[pp],PQ[cp] = PQ[cp],PQ[pp]
            QPos[PQ[pp][0]] = pp
            QPos[PQ[cp][0]] = cp
            cp = pp
        else:
            return
    return

def make_link(G, node1, node2, w):
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
def downHeapify(PQ,QPos,pp):
    lcp = 2*pp+1 #left child's position in PQ
    lenPQ = len(PQ)
    if lcp>=lenPQ:
        return
    pv = PQ[pp][1] #parent value
    rcp = 2*pp+2 #right childs position in PQ 
    lcv = PQ[lcp][1] #left child's value at it's position in PQ 
    if rcp>=lenPQ:
        if pv > lcv:  #moving/swapping down the tree
            PQ[lcp],PQ[pp]= PQ[pp],PQ[lcp]
            QPos[PQ[lcp][0]] = lcp
            QPos[PQ[pp][0]] = pp
        return
    rcv = PQ[rcp][1] #right child's value at it's position in PQ  
    if min(lcv,rcv) >= pv:
        return
    if lcv < rcv:
        PQ[lcp],PQ[pp]= PQ[pp],PQ[lcp]
        QPos[PQ[lcp][0]] = lcp
        QPos[PQ[pp][0]] = pp
        downHeapify(PQ,QPos,pp)
        return
    PQ[rcp],PQ[pp]= PQ[pp],PQ[rcp]
    QPos[PQ[rcp][0]] = rcp
    QPos[PQ[pp][0]] = pp
    downHeapify(PQ,QPos,pp)
    return

def insert(PQ,QPos,nodeID,value):
    p = len(PQ) #position where child is being add
    QPos[nodeID] = p
    PQ.append([nodeID,value])
    upHeapify(PQ,QPos,p)
    return

def removeMin(PQ,QPos):
    smallestNode = []+PQ[0]
    del QPos[PQ[0][0]]
    del PQ[0]
    if PQ:
        PQ.appendleft(PQ.pop())
        #PQ = []+PQ[:-1] #caused PQ to de-reference, so I decided to use deque
        QPos[PQ[0][0]] = 0
        downHeapify(PQ,QPos,0)
    return smallestNode[0],smallestNode[1]

def dijkstra(G,v):
    final_dist = {}
    PQ = deque([[v,0]])  #[ref, val]
    QPos = {v:0}   #queue positions for each element
    lenG = len(G)
    while len(final_dist) < lenG:
        w,final_dist[w] = removeMin(PQ,QPos)
        for x in G[w]:
            if x not in final_dist:
                value = final_dist[w] + G[w][x]
                if x not in QPos:
                    insert(PQ,QPos,x,value)
                elif value < PQ[QPos[x]][1]:
                    update(PQ,QPos,x,value) #... which finds it's pos, and calls downheapify
    return final_dist

def test2(N):
    # shortcuts
    nodes=list(range(1,N))
    edges=[]
    for i in range(5*N):
      u=randint(1,N)
      v=randint(1,N)
      if u!=v:
        edges.append((u,v,randint(1,10)))
    G = {}
    for (i,j,k) in edges:
        make_link(G, i, j, k)
    dist = dijkstra(G,1)

#test()

for N in [100,300,600,1000,3000,6000,10000,30000,60000,100000]:
#for N in [100,300,600,1000,3000,6000,10000]:
  print(N)
  test2(N)

