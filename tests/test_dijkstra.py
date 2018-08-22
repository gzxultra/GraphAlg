
from src.dijkstra import dijkstra


def test_dijkstra(graph):
    src, dst = 0, 2
    result = dijkstra(graph, src, dst)
    assert result == ({0: 0, 1: 100, 2: 300, 3: 200}, {0: None, 1: None, 2: 3, 3: 1})
