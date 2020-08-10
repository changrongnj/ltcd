'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        '''
        dfs
        '''
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, r, c):
        i, j = r, c
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] != "1":
            return
        if grid[i][j] == "1":
            grid[i][j] = "#"
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)


# BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        '''
        bfs
        '''
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    queue = [(i, j)]
                    beingVisited = set(queue)
                    while queue:
                        r, c = queue.pop(0)
                        grid[r][c] = "#"
                        locations = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for add_r, add_c in locations:
                            nr, nc = r + add_r, c + add_c
                            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                                continue
                            if grid[nr][nc] == "1" and (nr, nc) not in beingVisited:
                                queue.append((nr, nc))
                                beingVisited.add((nr, nc))
                    count += 1
        return count
