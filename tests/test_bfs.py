def test_bfs_iterative():
    from src.libs import Graph
    from src.bfs import bfs_iterative
    edges = [[1,2], [1,3], [2,4], [2,5], [3,6]]
    nodes = list(range(1, 6))
    src, dst = 1, 6
    graph = Graph()
    for node in nodes:
        graph.add_node(node)
    for (from_node, to_node) in edges:
        graph.add_edge(from_node, to_node)

    assert bfs_iterative(graph, src, dst) == [1, 2, 3, 4, 5, 6]
