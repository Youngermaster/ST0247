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
    ('Bodega 1', 'Almacen 1', 2),
    ('Bodega 1', 'Almacen 2', 3),
    ('Bodega 1', 'Almacen 3', 4),

    ('Almacen 1', 'Sucursal 1', 1),
    ('Almacen 1', 'Sucursal 2', 5),
    ('Almacen 1', 'Sucursal 3', 2),
    ('Almacen 1', 'Sucursal 4', 1),
    ('Almacen 1', 'Sucursal 5', 2),

    ('Almacen 2', 'Sucursal 1', 2),
    ('Almacen 2', 'Sucursal 2', 1),
    ('Almacen 2', 'Sucursal 3', 3),
    ('Almacen 2', 'Sucursal 4', 3),
    ('Almacen 2', 'Sucursal 5', 2),

    ('Almacen 3', 'Sucursal 1', 2),
    ('Almacen 3', 'Sucursal 2', 2),
    ('Almacen 3', 'Sucursal 3', 1),
    ('Almacen 3', 'Sucursal 4', 2),
    ('Almacen 3', 'Sucursal 5', 1),

    ('Sucursal 1', 'Tienda 1', 7),
    ('Sucursal 1', 'Tienda 2', 5),
    ('Sucursal 1', 'Tienda 3', 2),
    ('Sucursal 1', 'Tienda 4', 4),
    ('Sucursal 1', 'Tienda 5', 3),

    ('Sucursal 2', 'Tienda 1', 5),
    ('Sucursal 2', 'Tienda 2', 2),
    ('Sucursal 2', 'Tienda 3', 1),
    ('Sucursal 2', 'Tienda 4', 7),
    ('Sucursal 2', 'Tienda 5', 2),

    ('Sucursal 3', 'Tienda 1', 5),
    ('Sucursal 3', 'Tienda 2', 3),
    ('Sucursal 3', 'Tienda 3', 2),
    ('Sucursal 3', 'Tienda 4', 3),
    ('Sucursal 3', 'Tienda 5', 7),

    ('Sucursal 4', 'Tienda 1', 2),
    ('Sucursal 4', 'Tienda 2', 8),
    ('Sucursal 4', 'Tienda 3', 3),
    ('Sucursal 4', 'Tienda 4', 1),
    ('Sucursal 4', 'Tienda 5', 2),

    ('Sucursal 5', 'Tienda 1', 3),
    ('Sucursal 5', 'Tienda 2', 3),
    ('Sucursal 5', 'Tienda 3', 1),
    ('Sucursal 5', 'Tienda 4', 2),
    ('Sucursal 5', 'Tienda 5', 6),

    ('Tienda 1', 'Agencia 1', 2),
    ('Tienda 1', 'Agencia 2', 1),

    ('Tienda 2', 'Agencia 1', 6),
    ('Tienda 2', 'Agencia 2', 2),
    
    ('Tienda 3', 'Agencia 1', 5),
    ('Tienda 3', 'Agencia 2', 2),

    ('Tienda 4', 'Agencia 1', 3),
    ('Tienda 4', 'Agencia 2', 4),

    ('Tienda 5', 'Agencia 1', 8),
    ('Tienda 5', 'Agencia 2', 1),

    ('Agencia 1', 'Bodega 2', 4),

    ('Agencia 2', 'Bodega 2', 6),
    
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
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

print("\nPath from Bodega 1 to Bodega 2:\n")
print(core(graph, 'Bodega 1', 'Bodega 2'))