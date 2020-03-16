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
'''

# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        marked = [0 for _ in range(numCourses)]  #0 = not visited, -1 = visited, 1 = visiting

        graph = [[] for _ in range(numCourses)]  # build graph adjacency list
        for course, prereq in prerequisites: 
            graph[course].append(prereq)
        
        queue = [False]  #first element: cycle or not; topological order
        for course in range(numCourses):
            if marked[course] == 0:
                self.dfs(graph, course, marked, queue)
                
        if queue[0] == False:
            return queue[1:]
        else:
            return []
        
            
    def dfs(self, graph, course, marked, queue):
        marked[course] = 1
        if graph[course] != []:
            for prereq in graph[course]:
                if marked[prereq] == 0:
                    self.dfs(graph, prereq, marked, queue)
                if marked[prereq] == 1:
                    queue[0] = True
                    return
        queue.append(course)
        marked[course] = -1