'''
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graphAJ = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graphAJ[course].append(prereq)
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.DFS(graphAJ, i, visited):
                return False
        return True
    
    def DFS(self, graph, i, visited):
        if visited[i] == 1:  # is being visited
            return False
        if visited[i] == -1:  # has been visited
            return True
        visited[i] = 1
        for neighbor in graph[i]:
            if not self.DFS(graph, neighbor, visited):
                return False
        visited[i] = -1
        return True