class GraphException(Exception):
    pass


class Hypergraph:
    def __init__(self):
        self.nodes = {
            0: []
        }

        self.values = {}

        self.current = 0
        self.direction = None

    def add_node(self):
        self.nodes[max(self.nodes.keys())+1] = []
        self.values[max(self.nodes.keys())+1] = 0

    def turn_left(self):
        self.direction -= 1
        self.direction %= len(self.nodes[self.current])

    def turn_right(self):
        self.direction += 1
        self.direction %= len(self.nodes[self.current])

    def go(self):
        self.current = self.nodes[self.direction]
        self.direction = 0

    def increment(self):
        self.values[self.current] += 1

    def decrement(self):
        self.values[self.current] -= 1

    def connect(self, node):
        self.nodes[self.current].append(node)

    def disconnect(self, node):
        del self.nodes[self.current][self.nodes[self.current].find(node)]

    def destroy(self):
        last = self.current
        self.go()
