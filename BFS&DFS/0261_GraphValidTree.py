'''
261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.

Notice
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if n == 0:
            return False

        # n - 1 edges thus connected by no cycle
        if len(edges) != n - 1:
            return False
        # BFS
        # hashmap = {vertex : neighbor - connected vertices}
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # choose a node, whether this node could reach to all the other nodes
        visited = set([0])
        queue = [0]
        count = 0
        while queue:
            vertex = queue.pop(0)
            count += 1
            for neighbor in graph[vertex]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return count == n
