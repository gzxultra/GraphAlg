def dijkstra(G, src, dst):
    Q = list(G.nodes)
    dist, prev = {}, {}

    for v in Q:
        dist[v] = float('inf')
        prev[v] = None

    dist[src] = 0

    while Q:
        Q.sort(key=lambda x: dist.get(x, float('inf')), reverse=True)
        u = Q.pop()

        for v in G.edges[u]:
            alt = G.distances[(u,v)] + dist[u]

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


# defaultdict(list,
#             {0: [1, 1, 4, 2],
#              1: [2, 6, 5, 0],
#              2: [4, 5, 1, 0],
#              3: [7],
#              4: [0, 2],
#              5: [6, 2, 1],
#              6: [1, 5],
#              7: [3]})