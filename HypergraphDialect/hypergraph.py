def is_well_formed(graph):
        if type(graph) != dict:
            return False

        nodes = graph.keys()

        for vals in graph.values():
            if list(set(vals)) != vals:
                return False

            if not set(vals).issubset(set(nodes)):
                return False

        return True


class GraphException(Exception):
    pass


class Hypergraph:
    def __init__(self):
        self.values = [0]
        self.edges = [[]]
        self.current = 0
        self.direction = None

    def add_node(self):
        self.edges.append([])

    def connect_to_edge(self, edge):
        self.edges[edge].append(self.current)
