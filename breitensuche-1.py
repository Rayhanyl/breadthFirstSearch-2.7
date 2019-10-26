
def nachbarn_von(knoten, graph):
    return graph[knoten]


def breitensuche(graph, start_knoten):
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    while warteschlange:
        aktueller_knoten = warteschlange.pop(0)
        for nachbar in nachbarn_von(aktueller_knoten, graph):
            if nachbar not in besuchte_knoten:
                warteschlange.append(nachbar)
                besuchte_knoten.append(nachbar)
    return besuchte_knoten


def breitensucheAlpha(graph, start_knoten):
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    while warteschlange:
        aktueller_knoten = warteschlange.pop(0)
        for nachbar in nachbarn_von(aktueller_knoten, graph):
            warteschlange.append(nachbar)
            besuchte_knoten.append(nachbar)
    return besuchte_knoten


def pfad(eltern_dict, ziel_knoten):
    result = [ziel_knoten];
    vater = eltern_dict[ziel_knoten]
    while vater != None:
        result.append(vater)
        vater = eltern_dict[vater]
    result.reverse()
    return result


def kuerzester_weg(graph, start_knoten, ziel_knoten):
    if (start_knoten == ziel_knoten):
        return [start_knoten]
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    eltern_dict = {start_knoten: None}
    while warteschlange:
        aktueller_knoten = warteschlange.pop(0)
        for nachbar in graph[aktueller_knoten]:
            if (nachbar == ziel_knoten):
                besuchte_knoten.append(nachbar)
                eltern_dict[nachbar] = aktueller_knoten
                return pfad(eltern_dict, ziel_knoten)
            elif nachbar not in besuchte_knoten:
                warteschlange.append(nachbar)
                besuchte_knoten.append(nachbar)
                eltern_dict[nachbar] = aktueller_knoten
    return []


graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

graph_2 = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E', 'F'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'F', 'H'],
    'E': ['B', 'C', 'G'],
    'F': ['B', 'D', 'G', 'H', 'I'],
    'G': ['E', 'F', 'I'],
    'H': ['D', 'F'],
    'I': ['F', 'G']
}

graph_3 = {
    'A': ['B', 'D', 'F'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'I'],
    'D': ['A', 'E', 'F', 'G'],
    'E': ['B', 'C', 'D', 'G', 'H', 'I'],
    'F': ['A', 'D', 'G'],
    'G': ['D', 'E', 'F', 'H'],
    'H': ['E', 'G', 'I'],
    'I': ['C', 'E', 'H']
}

graph_4 = {
    'A': ['B'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'I'],
    'E': ['B'],
    'F': ['C'],
    'G': ['H'],
    'H': ['G', 'I'],
    'I': ['D', 'H', 'K'],
    'J': ['K'],
    'K': ['I', 'J', 'L'],
    'L': ['K']
}

print "Breitensuche graph_1: ", breitensuche(graph_1, 'A')
print "Breitensuche graph_2: ", breitensuche(graph_2, 'A')
print "Breitensuche graph_3: ", breitensuche(graph_3, 'A')
print "Breitensuche graph_4: ", breitensuche(graph_4, 'D')
print ""
print "Kuerzester Weg graph_3"
print "  von A nach D: ", kuerzester_weg(graph_3, 'A', 'D')  # A D
print "  von C nach F: ", kuerzester_weg(graph_3, 'C', 'F')  # C B A F
print "  von A nach H: ", kuerzester_weg(graph_3, 'A', 'H')  # A B D H
print "  von A nach Z: ", kuerzester_weg(graph_4, 'A', 'Z')  # A
print ""
print "Kuerzester Weg graph_4"
print "  von D nach J: ", kuerzester_weg(graph_4, 'D', 'J')  # D I K J
print "  von K nach F: ", kuerzester_weg(graph_4, 'K', 'F')  # K I D C F
print "  von E nach G: ", kuerzester_weg(graph_4, 'E', 'G')  # E B C D I H G
print "  von C nach C: ", kuerzester_weg(graph_4, 'C', 'C')  # C


