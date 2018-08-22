from src.bfs import bfs_iterative, bfs_recursive


def test_bfs_iterative(graph2):
    src, dst = 1, 6
    assert bfs_iterative(graph2, src, dst) == [1, 2, 3, 4, 5, 6]


def test_bfs_recursive(graph2):
    src, dst = 1, 6
    assert bfs_recursive(graph2, src, dst) == [1, 2, 3, 4, 5, 6]
