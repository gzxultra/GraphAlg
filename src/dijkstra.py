def dijkstra(G, src, dst):
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
