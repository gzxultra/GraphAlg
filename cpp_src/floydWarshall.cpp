#include "graph.h"
#include <vector>
#include <iostream>
#define INF (unsigned)!((int)0)


int** floydWarshall(Graph G) {
    vector<int> nodes = G.getAllNodes();
    int nNodes = nodes.size();
    int nEdges = G.getNEdges();
    vector<int> edgeFromNodes = G.getAllEdgeFromNodes();
    vector<int> edgeToNodes = G.getAllEdgeToNodes();
    int** dist = new int*[nNodes];
    for (int i=0; i<nNodes; i++) {
        dist[i] = new int[nNodes];
    }

    for (int i=0; i<nNodes; i++) {
        for (int j=0; j<nNodes; j++) {
            dist[i][j] = INF;
        }
    }

    for (int i=0; i<nEdges; i++) {
        dist[edgeFromNodes[i]][edgeToNodes[i]] = G.getEdgeDistance(edgeFromNodes[i], edgeToNodes[i]);
    }

    for (int v : nodes) {
        dist[v][v] = 0;
    }

    for (int k=0; k<nNodes; k++) {
        for (int i=0; i<nNodes; i++) {
            for (int j=0; j<nNodes; j++) {
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    return dist;
}

int main(int argc, char** argv) {
    Graph graph = Graph();
    // [[0,1,100],[0,3,300],[0,2,500],[1,3,100],[3,2,100]]
    int nNodes = 4;
    for (int node=0; node<nNodes; node++) {
        graph.addNode(node);
    }
    graph.addEdge(0, 1, 100);
    graph.addEdge(0, 3, 300);
    graph.addEdge(0, 2, 500);
    graph.addEdge(1, 3, 100);
    graph.addEdge(3, 2, 100);

    int** dist;
    dist = floydWarshall(graph);
    for (int i=0; i<nNodes; i++) {
        for (int j=0; j<nNodes; j++) {
            std::cout << dist[i][j];
        }
        std::cout << std::endl;
    }
}
