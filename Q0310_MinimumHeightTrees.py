'''
310. Minimum Height Trees
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
        
        # build graph
        G = [set() for _ in range(n)]
        degree = [0 for _  in range(n)]
        for v1, v2 in edges:
            G[v1].add(v2)
            degree[v1] += 1
            G[v2].add(v1)
            degree[v2] += 1
            
            
        # deleting leaves level by level till the middle layer:root or layers:root + node
        unvisited = set(range(n))
        leaves = set(v for v in unvisited if degree[v] == 1)
        while len(unvisited) > 2:
            newLeaves = set()
            unvisited -= leaves
            for v in leaves:
                for nei in G[v]: #for any connection of v
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        newLeaves.add(nei)
            leaves = newLeaves
        return list(leaves)

       

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build graph
        G = [set() for _ in range(n)]
        for v1, v2 in edges:
            G[v1].add(v2)
            G[v2].add(v1)
            
        # deleting leaves level by level till the middle layer:root or layers:root + node
        unvisited = set(i for i in range(n))
        while len(unvisited) > 2:
            leaves = set(i for i in unvisited if len(G[i]) == 1)
            unvisited -= leaves
            for v in leaves:
                for nei in G[v]: #for any connection of v
                    G[nei].remove(v) # remove v from its connection in graph adjacency list
        return list(unvisited)

       