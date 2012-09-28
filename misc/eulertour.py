# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1),(]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    return []

def find_degrees(graph):
    degrees = {}
    for edge in graph:
        if edge[0] in degrees:
            degrees[edge[0]] += 1
        else : 
            degrees[edge[0]] = 1
        if edge[1] in degrees:
            degrees[edge[1]] += 1
        else : 
            degrees[edge[1]] = 1
    print degrees
    return degrees

def is_eul_path_exist(graph):
    degrees = find_degrees(graph)
    for node in degrees:
        if degrees[node]%2 !=0 :
            return False
    return True


print is_eul_path_exist([(1, 2), (2, 3), (3, 1),(3,4),(4,5),(5,6),(6,3)])

