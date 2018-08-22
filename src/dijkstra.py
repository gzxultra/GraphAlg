from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.adjacents = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.adjacents[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance



def dijkstra(G):
    Q = G.nodes
    dist, prev = {}, {}

    for v in Q:
        dist[v] = G.distances.get((src, v)) or float('inf')
        prev[v] = None

    dist[src] = 0
    Q.remove(src)

    while Q:
        u, cost = None, float('inf')
        for node in Q:
            if node == src or not G.distances[(src, node)]:
                continue
            if G.distances[(src, node)] < cost:
                u, cost = node, G.distances[(src, node)]
        if not u:
            break

        Q.remove(u)

        for v in G.edges[u]:
            alt = G.distances[(u,v)] + dist[u]

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev
