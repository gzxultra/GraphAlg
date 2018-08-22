from src.floyd_warshall import floyd_warshall


def test_floyd_warshall(graph1):
    dist = floyd_warshall(graph1)

    assert dist[0][2] == 300
    assert dist[0][3] == 200
    assert dist[1][2] == 200
