'''
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

# BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            course = queue.pop(0)
            res.append(course)
            for nextPossbleCourse in graph[course]:
                indegree[nextPossbleCourse] -= 1
                if indegree[nextPossbleCourse] == 0:
                    queue.append(nextPossbleCourse)

        if len(res) == numCourses:
            return res
        return []


# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            
        res = []
        visited = [0 for _ in range(numCourses)]
        for course in range(numCourses):
            if not self.dfs(course, graph, res, visited):
                return []

        return res[::-1]
 
    
    def dfs(self, course, graph, res, visited):
        if visited[course] == 1: # being visited
            return False
        if visited[course] == -1:
            return True
        visited[course] = 1
        if graph[course]:
            for nextCourse in graph[course]:
                if not self.dfs(nextCourse, graph, res, visited):
                    return False
        visited[course] = -1
        res.append(course)
        return True
