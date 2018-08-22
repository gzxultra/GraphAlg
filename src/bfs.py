from collections import deque


def bfs_iterative(G, src, dst):
    visited, queue = [], deque()
    queue.appendleft(src)

    while queue:
        node = queue.pop()
        visited.append(node)

        if node == dst:
            return visited

        for edge in G.edges[node]:
            queue.appendleft(edge)
    return None


def bfs_recursive(G, src, dst):
    visited = []

    def bfs(G, src, dst, visited=None):
        if visited is None:
            visited = []
        visited.append(src)

        for edge in set(G.edges[src]):
            if edge in visited:
                continue
            bfs(G, edge, dst, visited)

        return visited

    return bfs(G, src, dst)
