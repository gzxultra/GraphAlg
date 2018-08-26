#include <vector>
using namespace std;


class Graph {
    private:
        int nNodes;
        int nEdges;
        vector<int> nodes;
        vector<int> edgeFromNodes;
        vector<int> edgeToNodes;
        vector<int> edgeDistances;
    public:
        void addNode(int value);
        void addEdge(int fromNode, int toNode, int value);
        vector<int> getAllNodes();
        int getEdgeDistance(int edgeFromNode, int edgeToNode);
        int getNEdges();
        vector<int> getAllEdgeFromNodes();
        vector<int> getAllEdgeToNodes();
};
