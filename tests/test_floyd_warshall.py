from src.floyd_warshall import (floyd_warshall,
    floyd_warshall_with_path_reconstruction, reconstruct_path)


def test_floyd_warshall(graph1):
    dist = floyd_warshall(graph1)

    assert dist[0][2] == 300
    assert dist[0][3] == 200
    assert dist[1][2] == 200


def test_floyd_warshall_with_path_reconstruction(graph1):
    dist, next_move = floyd_warshall_with_path_reconstruction(graph1)

    path = reconstruct_path(next_move, 0, 3)
    assert path == [0, 1, 3]

    path = reconstruct_path(next_move, 0, 2)
    assert path == [0, 1, 3, 2]
