'''
863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  
The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 
Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []

        '''
        return a dictionary: {node:neighbors}
        '''
        def buildGraph(node, parent, graph):
            if not node:
                return
            if node not in graph:
                graph[node] = []
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            buildGraph(node.left, node, graph)
            buildGraph(node.right, node, graph)

        graph = dict()
        buildGraph(root, None, graph)

        queue, visited = [target], set([target])  # BFS
        while queue:
            if K == 0:
                return [queue[i].val for i in range(len(queue))]
            K -= 1
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
        return []
