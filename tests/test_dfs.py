from src.dfs import dfs_recursive, dfs_iterative


def test_dfs_recursive(graph2):
    src, dst = 1, 6
    assert dfs_recursive(graph2, src, dst) == [1, 2, 4, 5, 3, 6]


def test_dfs_iterative(graph2):
    src, dst = 1, 6
    assert dfs_iterative(graph2, src, dst) == [1, 2, 4, 5, 3, 6]
