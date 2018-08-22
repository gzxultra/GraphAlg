import pytest
from src.libs import Graph


@pytest.fixture(scope="session")
def graph1():
    n_nodes = 4
    edges = [[0,1,100],[0,3,300],[0,2,500],[1,3,100],[3,2,100]]

    graph = Graph()
    for node in range(0, n_nodes):
        graph.add_node(node)
    for (from_node, to_node, distance) in edges:
        graph.add_edge(from_node, to_node, distance)

    yield graph


@pytest.fixture(scope="session")
def graph2():
    n_nodes = 6
    edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]]

    graph = Graph()
    for node in range(1, n_nodes):
        graph.add_node(node)
    for (from_node, to_node) in edges:
        graph.add_edge(from_node, to_node)

    yield graph

