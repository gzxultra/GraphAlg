def dfs_iterative(G, src, dst):
    visited, stack = [], [src]

    while stack:
        node = stack.pop()
        visited.append(node)

        if node == dst:
            return visited

        for edge in reversed(G.edges[node]):
            stack.append(edge)
    return visited


def dfs_recursive(G, src, dst):
    visited = []

    def dfs(G, src, dst):
        visited.append(src)

        for edge in set(G.edges[src]):
            if edge in visited:
                continue
            dfs(G, edge, dst)

        return visited

    return dfs(G, src, dst)
