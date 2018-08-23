def floyd_warshall(G):
    """ Floyd–Warshall algorithm
        pseudocode by wikipedia: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    """
    n_nodes = len(G.nodes)
    dist = [[float('inf') for i in range(0, n_nodes)] for j in range(0, n_nodes)]

    for from_node in G.nodes:
        for to_node in G.edges[from_node]:
            dist[from_node][to_node] = G.distances[(from_node, to_node)]

    for k in G.nodes:
        for i in G.nodes:
            for j in G.nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def floyd_warshall_with_path_reconstruction(G):
    """ Floyd–Warshall algorithm
        pseudocode by wikipedia: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    """
    n_nodes = len(G.nodes)
    dist = [[float('inf') for i in range(0, n_nodes)] for j in range(0, n_nodes)]
    next_move = [[float('inf') for i in range(0, n_nodes)] for j in range(0, n_nodes)]

    for from_node in G.nodes:
        for to_node in G.edges[from_node]:
            dist[from_node][to_node] = G.distances[(from_node, to_node)]
            next_move[from_node][to_node] = to_node

    for k in G.nodes:
        for i in G.nodes:
            for j in G.nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_move[i][j] = next_move[i][k]
    return dist, next_move


def reconstruct_path(next_move, u, v):
    if not next_move[u][v]:
        return []

    path = [u]
    while u != v:
        u = next_move[u][v]
        path.append(u)
    return path
