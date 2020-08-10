'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 
Constraints:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
'''
# DFS


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        graph = {prerequisite course : courses}
        '''
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        # dfs to search for cycle
        visited = [0 for _ in range(numCourses)]
        for course in range(numCourses):
            if not self.isCycle(course, graph, visited):
                return False
        return True

    def isCycle(self, course, graph, visited):
        if visited[course] == -1:
            return True
        if visited[course] == 1:  # is being visited as a prerequisite course.
            return False
        visited[course] = 1
        for nextPossibleCourse in graph[course]:
            if not self.isCycle(nextPossibleCourse, graph, visited):
                return False
        visited[course] = -1
        return True


# BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        graph = {prerequisite course : courses}
        '''
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # bfs
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = []
        while queue:
            course = queue.pop(0)
            visited.append(course)
            for nextPossibleCourse in graph[course]:
                indegree[nextPossibleCourse] -= 1
                if indegree[nextPossibleCourse] == 0:
                    queue.append(nextPossibleCourse)

        if len(visited) == numCourses:
            return True
        return False
