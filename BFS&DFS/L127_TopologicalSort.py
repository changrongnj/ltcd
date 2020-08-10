'''
127. Topological Sorting
Given an directed graph, a topological order of the graph nodes is defined as follow:
For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
The topological order can be:
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...

Notice
You can assume that there is at least one topological order in the graph.
'''
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# BFS
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # find the first node from indegree
        indegree = dict()
        res = []
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in indegree:
                    indegree[neighbor] += 1
                else:
                    indegree[neighbor] = 1

        queue = []
        for node in graph:
            if node not in indegree:
                queue.append(node)

        while queue:
            node = queue.pop(0)
            res.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) == len(graph):
            return res
        return []


# DFS
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):

        res = []
        visited = set()

        # dfs
        # define recursion

        def dfs(node, visited, res):
            # exit
            if node in visited:
                return
            visited.add(node)
            if not node.neighbors:
                res.append(node)
                return
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor, visited, res)
            res.append(node)

        for v in graph:
            if v not in visited:
                dfs(v, visited, res)

        return res[::-1]
