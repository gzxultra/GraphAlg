#include "graph.h"

using namespace std;

void Graph::addNode(int node) {
    nodes.push_back(node);
    nNodes ++;
}

void Graph::addEdge(int edgeFromNode, int edgeToNode, int edgeDistance) {
    edgeFromNodes.push_back(edgeFromNode);
    edgeToNodes.push_back(edgeToNode);
    edgeDistances.push_back(edgeDistance);
    nEdges ++;
}

vector<int> Graph::getAllNodes() {
    return nodes;
}

int Graph::getEdgeDistance(int edgeFromNode, int edgeToNode) {
    for (int i=0; i < nEdges; i++) {
        if (edgeFromNodes[i] == edgeFromNode and edgeToNodes[i] == edgeToNode) {
            return edgeDistances[i];
        }
    }
}

int Graph::getNEdges() {
    return nEdges;
}

vector<int> Graph::getAllEdgeFromNodes() {
    return edgeFromNodes;
}

vector<int> Graph::getAllEdgeToNodes() {
    return edgeToNodes;
}
