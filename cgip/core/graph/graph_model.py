class Graph:
    """
    Moteur de graphe Core (Minimal Viable System).
    Totalement indépendant des modules ML pour garantir la stabilité.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, n):
        self.nodes.add(n)

    def add_edge(self, a, b, t="related"):
        self.edges.append((a, b, t))
