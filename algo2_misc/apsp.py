def apsp(G):
    l = len(G) + 1
    g = range(1, l)
    dist = []
    dist.append([[99999999]*l]*l)
    dist.append([[99999999]*l]*l)
    for i in g:
        for j in g:
            if i == j:
                dist[1][i][j] = 0
            elif i in G and j in G[i]:
                dist[1][i][j] = G[i][j]
            else:
                dist[1][i][j] = 99999999
    for i in g:
        print i
        for j in g:
            for k in g:
                dist[0][i][j] = dist[1][i][j]
            for k in g:
                dist[1][i][j] = min(dist[0][i][j], dist[0][i][k] + dist[0][k][j])
    return dist[1]

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def main ():
    f = open('e:\\g4.txt' , 'r')
    
    head = 0
    
    G = {}
    
    for i in f:
        if head != 0:
            s = i.strip().split(' ')
            make_link(G, int(s[0]), int(s[1]), int(s[2]))
        head += 1
    
    a = apsp(G)   
    print a
    print min(a)
    
    cycle = False
    
    minimum = 9999999999
    
    for i in range(1,len(G)):
        for j in range(1,len(G)):
            if i == j and a[i][j] < 0:
                cycle = True
            else:
                if minimum > a[i][j]:
                    minimum = a[i][j]
            
    print cycle
    print min(a[i][j])

if __name__ == "__main__":
    main()  
                