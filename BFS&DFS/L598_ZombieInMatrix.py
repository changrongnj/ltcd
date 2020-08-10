'''
598. Zombie in Matrix
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 
(the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, 
but can not through wall. How long will it take to turn all people into zombies? 
Return -1 if can not turn all people into zombies.

Example
Example 1:

Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
Example 2:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
'''


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):

        if not grid or not grid[0]:
            return -1

        zombies = []
        pplCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    zombies.append((i, j))
                if grid[i][j] == 0:
                    pplCount += 1

        dayCount = 0
        pplTurned = 0
        visited = set()
        while zombies:
            visited.update(set(zombies))
            level = zombies
            zombies = []
            dayCount += 1
            for zr, zc in level:
                dirs = [(zr - 1, zc), (zr + 1, zc), (zr, zc - 1), (zr, zc + 1)]
                for r, c in dirs:
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                        continue
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                        pplTurned += 1
                        if (r, c) not in visited:
                            zombies.append((r, c))
            if pplTurned == pplCount:
                return dayCount
        return -1
