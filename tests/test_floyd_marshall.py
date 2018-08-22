from src.floyd_marshall import floyd_marshall


def test_floyd_marshall(graph1):
    dist = test_floyd_marshall(graph1)

    assert dist[0][2] == 300
    assert dist[0][3] == 200
    assert dist[1][2] == 200
