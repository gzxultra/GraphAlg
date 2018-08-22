from src.bfs import bfs_iterative


def test_bfs_iterative(graph2):
    src, dst = 1, 6
    assert bfs_iterative(graph2, src, dst) == [1, 2, 3, 4, 5, 6]
