
if __name__ == '__main__':

    f = open('//home//rejith//Downloads//g3.txt' , 'r')
    head = 0
    G1 = numpy.arange(1000000)
    G = G1.reshape(1000,1000)
    INF = 999
    vertices = []

    for i in f:
        if head != 0:
            if int(i.strip().split(' ')[0]) not in vertices:
                vertices.append(int(i.strip().split(' ')[0]) )
            if int(i.strip().split(' ')[1]) not in vertices:
                vertices.append(int(i.strip().split(' ')[1]) )
        head += 1

    l = range(len(vertices))

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j:
                G[i][j] = INF


    f = open('//home//rejith//Downloads//g3.txt' , 'r')
    head = 0

    for i in f:
        if head != 0:
            s = i.strip().split(' ')
            G[int(s[0]) - 1][int(s[1]) - 1] = int(s[2])
        head += 1


    for k in l:
        print k
        for i in l:
            for j in l:
                G[i][j] = min (G[i][j], G[i][k] + G[k][j]);

    neg_cycle = False

    for i in l:
        if G[i][i] != 0:
            neg_cycle =  True
            break
    print 'Has negative cycle' , neg_cycle

    short_distance = INF

    if not neg_cycle:
        for i in l:
            for j in l:
                if G[i][j] < short_distance:
                    short_distance = G[i][j]

    print 'Short distance', short_distance
