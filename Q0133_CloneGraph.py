'''
133. Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
# DFS

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        root = Node(node.val, [])  # deep copy of the root node
        nodesCopy = {node: root}  
        # a dict collection of all newly created nodes
        # key: older nodes  value: deep copied new nodes
        s = [node]
        while s:
            currentNode = s.pop()
            for neiNode in currentNode.neighbors:
                if neiNode not in nodesCopy:
                    neiNodeCopy = Node(neiNode.val, [])
                    nodesCopy[neiNode] = neiNodeCopy
                    nodesCopy[currentNode].neighbors.append(neiNodeCopy)
                    s.append(neiNode)
                else:
                    nodesCopy[currentNode].neighbors.append(nodesCopy[neiNode])
        return root