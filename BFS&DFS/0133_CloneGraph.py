'''
133. Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


Constraints:
1 <= Node.val <= 100
Node.val is unique for each node.
Number of Nodes will not exceed 100.
There is no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None

        def getNodes(node):
            queue = [node]
            visited = set(queue)
            while queue:
                node = queue.pop(0)
                for neighbor in node.neighbors:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            # from a node to return a list of nodes in the graph
            return list(visited)

        raw = getNodes(node)

        # build the dictionary of clone nodes key:value = original node : clone node
        clone = {raw[i]: Node(raw[i].val) for i in range(len(raw))}

        # build nodes edges
        for rawNode in clone:
            for rawNeighbor in rawNode.neighbors:
                clone[rawNode].neighbors.append(clone[rawNeighbor])

        return clone[node]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        copy = {node: Node(node.val)}
        queue = [node]
        while queue:
            raw = queue.pop(0)
            if raw not in copy:
                copy[raw] = Node(raw.val)
            for rawNeighbor in raw.neighbors:
                if rawNeighbor not in copy:
                    copyNeighbor = Node(rawNeighbor.val)
                    copy[rawNeighbor] = copyNeighbor
                    queue.append(rawNeighbor)
                copy[raw].neighbors.append(copy[rawNeighbor])

        return copy[node]
