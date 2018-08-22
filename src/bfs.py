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
    return visited
