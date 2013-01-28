
# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#

import cPickle,itertools, operator

def create_weighted_graph(bipartiteG, characters):
    G = {}
    chars_G = {}
    comic_G = {}
    chars_no_comic = {}

    for i in bipartiteG:
        if i in characters:
            chars_G[i] = bipartiteG[i]
            chars_no_comic[i] =  bipartiteG[i].keys()
        else:
            comic_G[i] = bipartiteG[i]
    for j in comic_G:
        for i in  itertools.combinations(comic_G[j].keys(),2):
            if i in G:
                G[i] +=1 
            else:
                G[i] = 1
            if (i[1],i[0]) in G:
                G[(i[1],i[0])] +=1
            else:
                G[(i[1],i[0])]  = 1
    R = {}
    for i in G:
        if i[0] in R:
            R[i[0]][i[1]] = G[i]/(   len(list( set(chars_no_comic[i[0]]) |  set(chars_no_comic[i[1]])))   + 0.0)
        else:
            R[i[0]] = {i[1] : G[i]/(  len(list( set(chars_no_comic[i[0]]) |  set(chars_no_comic[i[1]])))   + 0.0)}
    return R

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None
    print G

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def test2():
    #marvel = cPickle.load(open("marvel", 'rb'))
    #characters = cPickle.load(open("chars",'rb'))
    comic_book = open('//home//rejith//Downloads//file' , 'r')
    chars = []
    G = {}
    for i in comic_book:
        make_link(G, i.split('\t')[0].strip() , i.split('\t')[1].strip())
        if i.split('\t')[0].strip() not in chars:
            chars.append(i.split('\t')[0].strip() )

    

    G = create_weighted_graph(G, chars)
    print G['"THING/BENJAMIN J. GR"']['"HUMAN TORCH/JOHNNY S"']
    print G['"HUMAN TORCH/JOHNNY S"']['"THING/BENJAMIN J. GR"']

   
test()
test2()