# Turning Back Time 
#
# Focus: Units 1, 2 and 3: Finite State Machines and List Comprehensions
#
#
# For every regular language, there is another regular language that all of
# the strings in that language, but reversed. For example, if you have a
# regular language that accepts "Dracula", "Was" and "Here", there is also
# another regular language that accepts exactly "alucarD", "saW" and
# "ereH". We can imagine that this "backwards" language is accepted by a
# "backwards" finite state machine.
#
# In this problem you will construct that "backwards" finite state machine. 
# Given a non-deterministic finite state machine, you will write a
# procedure reverse() that returns a new non-deterministic finite state
# machine that accepts all of the strings in the first one, but with their
# letters in reverse order. 
#
# We will use same the "edges" encoding from class, but we
# will make the start and accepting state explicit.  For example, the
# regular expression r"a(?:bx|by)+c" might be encoded like this:

edges = { (1,'a') : [2],
          (2,'b') : [3,4],
          (3,'x') : [5],
          (4,'y') : [5],
          (5,'b') : [3,4], 
          (5,'c') : [6],
          } 
accepting = 6 
start = 1 

# For this problem we will restrict attention to non-deterministic finite
# state machines that have a single start state and a single accepting
# state. Similarly, we will not consider epsilon transitions.
#
# For the example above, since the original NFSM accepts "abxc", the NFSM
# you produce must accept "cxba". Similarly, since the original accepts
# "abxbyc", the NFSM you produce must accept "cybxba", and so on. 
#
# Your procedure "reverse(edges,accepting,start)" should return a tuple
# (new_edges,new_accepting,new_start) that defines a new non-deterministic
# finite state machine that accepts every string in the language of the
# original ... reversed! 
#
# Vague Hint: Draw a picture, and then draw all the arrows backwards. 

def reverse(edges,accepting,start): 
        new_start = accepting
        new_accepting = start
        new_edges = {}
        for e in edges:
            for d in edges[e]:
                if (d,e[1]) not in new_edges:
                    new_edges[(d,e[1])] = [e[0]]
                else:
                    new_edges[(d,e[1])].append(e[0])
        return new_edges,new_accepting,new_start
                

# We have included some testing code to help you check your work. Since
# this is the final exam, you will definitely want to add your own tests.
#
# Recall: "hello"[::-1] == "olleh" 

def nfsmaccepts(edges,accepting,current,str): 
        if str == "":
                return current == accepting
        letter = str[0]
        rest = str[1:] 
        if (current,letter) in edges:
                for dest in edges[(current,letter)]:
                        if nfsmaccepts(edges,accepting,dest,rest):
                                return True
        return False
        
r_edges, r_accepting, r_start = reverse(edges,accepting,start) 

for s in [ "abxc", "abxbyc", "not", "abxbxbxbxbxc", "" ]: 
        # The original should accept s if-and-only-if the
        # reversed version accepts s_reversed. 
        print nfsmaccepts(edges,accepting,start,s) == \
              nfsmaccepts(r_edges,r_accepting,r_start,s[::-1])

# r"a+b*"
edges2 = { (1,'a') : [2],
          (2,'a') : [2],
          (2,'b') : [2] 
          } 
accepting2 = 2 
start2 = 1 

r_edges2, r_accepting2, r_start2 = reverse(edges2,accepting2,start2) 

for s in [ "aaaab", "aabbbbb", "ab", "b", "a", "", "ba" ]: 
        print nfsmaccepts(edges2,accepting2,start2,s) == \
        nfsmaccepts(r_edges2,r_accepting2,r_start2,s[::-1])



def nfsmaccepts2(edges, accepting, current, string, visited): 
        # If we have visited this state before, return false. 
        if (current, string) in visited:
                return False
        visited.append((current, string))

        # Check all outgoing epsilon transitions (letter == None) from this
        # state. 
        if (current, None) in edges:
                for dest in edges[(current, None)]:
                        if nfsmaccepts(edges, accepting, dest, string, visited):
                                return True

        # If we are out of input characters, check if this is an
        # accepting state. 
        if string == "":
                return current in accepting

        # If we are not out of input characters, try all possible
        # outgoing transitions labeled with the next character. 
        letter = string[0]
        rest = string[1:]
        if (current, letter) in edges:
                for dest in edges[(current, letter)]:
                        if nfsmaccepts(edges, accepting, dest, rest, visited):
                                return True
        return False

nfsmaccepts = nfsmaccepts2

# (ab)|((cd)*)
edges3 = {
    (1, None) : [4],
    (3, None) : [7],
    (5, 'd') : [6],
    (6, None) : [4],
    (2, 'b') : [3],
    (4, None) : [7],
    (4, 'c') : [5],
    (1, 'a') : [2]
}
accepting3 = 7 
start3 = 1

r_edges3, r_accepting3, r_start3 = reverse(edges3,accepting3,start3)

for s in [ "ab", "abc", "cd", "cdcd", "a", "", "ba" ]: 
        #print s, nfsmaccepts(edges3,[accepting3],start3,s,[])
        print nfsmaccepts(edges3,[accepting3],start3,s,[]) == \
        nfsmaccepts(r_edges3,[r_accepting3],r_start3,s[::-1],[])

# (a*b)|((cd)*)
edges3 = {
    (1, None) : [2, 5],
    (3, None) : [2],
    (5, None) : [8],
    (2, 'a') : [3],
    (2, 'b') : [4],
    (7, None) : [5],
    (4, None) : [8],
    (5, 'c') : [6],
    (6, 'd') : [7]
}
accepting3 = 8
start3 = 1

r_edges3, r_accepting3, r_start3 = reverse(edges3,accepting3,start3)

for s in [ "ab", "aaaab", "abc", "cd", "cda", "cdcd", "a", "", "ba" ]: 
        #print s, nfsmaccepts(edges3,[accepting3],start3,s,[])
        print nfsmaccepts(edges3,[accepting3],start3,s,[]) == \
        nfsmaccepts(r_edges3,[r_accepting3],r_start3,s[::-1],[])