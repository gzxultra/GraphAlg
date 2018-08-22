

def test_dijkstra():
    from src.dijkstra import dijkstra
    from src.libs import Graph

    n_cities = 4
    flights = [[0,1,100],[0,3,300],[0,2,500],[1,3,100],[3,2,100]]
    src, dst = 0, 2

    graph = Graph()
    for node in range(0, n_cities):
        graph.add_node(node)
    for (_src, _dist, _cost) in flights:
        graph.add_edge(_src, _dist, _cost)
    result = dijkstra(graph, src, dst)
    assert result == ({0: 0, 1: 100, 2: 300, 3: 200}, {0: None, 1: None, 2: 3, 3: 1})
