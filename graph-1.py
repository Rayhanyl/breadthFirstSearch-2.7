
def nachbarn_von(knoten, graph):
    return graph[knoten]


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

print "Nachbarn von A: ", nachbarn_von('A', graph)
print "Nachbarn von B: ", nachbarn_von('B', graph)
print "Nachbarn von C: ", nachbarn_von('C', graph)
print "Nachbarn von D: ", nachbarn_von('D', graph)
print "Nachbarn von E: ", nachbarn_von('E', graph)

