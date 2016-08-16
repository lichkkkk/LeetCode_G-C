/**
 * 133. Clone Graph
 * 
 * Chang Li @ Sunnyvale
 *
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    using Node = UndirectedGraphNode;
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node == nullptr) return nullptr;
        node_map[node] = new Node(node->label);
        noncloned_nodes.push(node);
        while (noncloned_nodes.size() > 0) {
            Node* next = noncloned_nodes.front();
            noncloned_nodes.pop();
            Node* cloned = GetClonedNode(next);
            for (Node* neighbor : next->neighbors) {
                cloned->neighbors.push_back(GetClonedNode(neighbor));
            }
        }
        return node_map[node];
    }
    
    Node* GetClonedNode(Node* node) {
        if (node_map.find(node) == node_map.end()) {
            node_map[node] = new Node(node->label);
            noncloned_nodes.push(node);
        }
        return node_map[node];
    }
    
private:
    unordered_map<Node*, Node*> node_map;
    queue<Node*> noncloned_nodes;
};
