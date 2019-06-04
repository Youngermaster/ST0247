from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph()

edges = [
    ('1', '2', 7),
    ('1', '3', 19),
    ('1', '4', 27),
    ('1', '5', 17),

    ('2', '1', 7),
    ('2', '3', 12),
    ('2', '4', 15),
    ('2', '5', 10),

    ('3', '1', 19),
    ('3', '2', 12),
    ('3', '4', 8),
    ('3', '5', 14),

    ('4', '1', 27),
    ('4', '2', 15),
    ('4', '3', 8),
    ('4', '5', 10),

    ('5', '1', 17),
    ('5', '2', 10),
    ('5', '3', 14),
    ('5', '4', 10),

]

for edge in edges:
    graph.add_edge(*edge)

def core(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    car = []
    while current_node is not None:
        path.append(current_node)
        if len(car) <= 5:
            car.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    car = car[::-1]
    car.pop()
    print("Car -> ", car)
    return path

print("\nPath from 4 to 1:\n")
print(core(graph, '4', '1'))
print("\nPath from 3 to 1:\n")
print(core(graph, '3', '1'))
print("\nPath from 5 to 1:\n")
print(core(graph, '5', '1'))
print("\nPath from 2 to 1:\n")
print(core(graph, '2', '1'))