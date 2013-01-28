import itertools, operator

comic_book = open('//home//rejith//Downloads//file' , 'r')


def make_link(G, node1, node2):
    #if node1 not in G:
    #    G[node1] = {}
    #(G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


G = {}

pairs = {}

for i in comic_book:
  make_link(G, i.split('\t')[0].strip() , i.split('\t')[1].strip())

print len(G)

for j in G:
    for i in  itertools.combinations(G[j].keys(),2):
        if i in pairs:
            pairs[i] +=1 
        else:
            pairs[i] = 1
        if (i[1],i[0]) in pairs:
            pairs[(i[1],i[0])] +=1
        else:
            pairs[(i[1],i[0])]  = 1


left = {}

right = {}


count = 0
for i in sorted(pairs.iteritems(), key=operator.itemgetter(1), reverse=True):
    print i
    count += 1
    if count > 10:
        break

print len(left)
print len(right)

pairs2 = {}

for i in pairs:
    j = tuple(sorted(i))
    pairs2[j] = pairs[i]

chars = open('//home//rejith//python//chars.txt','w')
graph = open('//home//rejith//python//graph.txt','w')


'''for i in pairs:
    if i[0] not in left:
        left[i[0]] = 1
        chars.write(str(i[0]))

for i in pairs:
    if i[1] not in right:
        right[i[1]] = 1
        chars.write(str(i[1]))

for i in pairs:
    graph.write(i)
    graph.write(pairs[i])'''

for i in pairs2:
    
    if i[0] == '"VESPER"' or i[1] == '"VESPER"':
        print i,pairs2[i]

graph.close()
chars.close()
