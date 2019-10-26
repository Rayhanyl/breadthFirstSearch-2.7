
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


def pfad(eltern_dict, ziel_knoten):
    result = [ziel_knoten];
    vater = eltern_dict[ziel_knoten]
    while vater is not None:
        result.append(vater)
        vater = eltern_dict[vater]
    result.reverse()
    return result


def ist_weg_vorhanden(graph, start_knoten, ziel_knoten):
    if start_knoten == ziel_knoten:
        return True
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    while warteschlange:
        aktueller_knoten = warteschlange.pop(0)
        for nachbar in nachbarn_von(aktueller_knoten, graph):
            if nachbar == ziel_knoten:
                return True
            elif nachbar not in besuchte_knoten:
                warteschlange.append(nachbar)
                besuchte_knoten.append(nachbar)
    return False


def kuerzester_weg(graph, start_knoten, ziel_knoten):
    if start_knoten == ziel_knoten:
        return [start_knoten]
    warteschlange = [start_knoten]
    besuchte_knoten = [start_knoten]
    eltern_dict = {start_knoten: None}
    while warteschlange:
        aktueller_knoten = warteschlange.pop(0)
        for nachbar in nachbarn_von(aktueller_knoten, graph):
            if nachbar == ziel_knoten:
                besuchte_knoten.append(nachbar)
                eltern_dict[nachbar] = aktueller_knoten
                return pfad(eltern_dict, ziel_knoten)
            elif nachbar not in besuchte_knoten:
                warteschlange.append(nachbar)
                besuchte_knoten.append(nachbar)
                eltern_dict[nachbar] = aktueller_knoten
    return []


graph_1 = {
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

graph_2 = {
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

print "Breitensuche in graph_1: ", breitensuche(graph_1, 'A')  # A B D F C E G I H
print "Breitensuche in graph_2: ", breitensuche(graph_2, 'D')  # D C I B F H K A E G J L
print ""
print "Wegsuche in graph_1"
print "  von A nach D: ", ist_weg_vorhanden(graph_1, 'A', 'D')  # True
print "  von A nach A: ", ist_weg_vorhanden(graph_1, 'A', 'A')  # True
print "  von A nach Z: ", ist_weg_vorhanden(graph_1, 'A', 'Z')  # False
print ""
print "Kuerzester Weg in graph_1"
print "  von A nach D: ", kuerzester_weg(graph_1, 'A', 'D')  # A D
print "  von C nach F: ", kuerzester_weg(graph_1, 'C', 'F')  # C B A F
print "  von A nach H: ", kuerzester_weg(graph_1, 'A', 'H')  # A B D H
print "  von A nach Z: ", kuerzester_weg(graph_2, 'A', 'Z')  # A
print ""
print "Kuerzester Weg in graph_2"
print "  von D nach J: ", kuerzester_weg(graph_2, 'D', 'J')  # D I K J
print "  von K nach F: ", kuerzester_weg(graph_2, 'K', 'F')  # K I D C F
print "  von E nach G: ", kuerzester_weg(graph_2, 'E', 'G')  # E B C D I H G
print "  von C nach C: ", kuerzester_weg(graph_2, 'C', 'C')  # C

print "Nachbarn von B: ", graph_2['B']
