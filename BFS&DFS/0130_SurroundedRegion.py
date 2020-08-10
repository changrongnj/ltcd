'''
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not 
flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

# BFS - starting with those border 'O" to find another "o"s connected


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        '''
        starting from the border 'O' to find all the 'O' not need to be switched
        '''
        nrow, ncol = len(board), len(board[0])
        queue = []
        for i in range(nrow):  # left and right border
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][ncol - 1] == 'O':
                queue.append((i, ncol - 1))
        for j in range(ncol):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[nrow - 1][j] == 'O':
                queue.append((nrow - 1, j))

        visited = set(queue)
        while queue:
            r, c = queue.pop(0)
            board[r][c] = 'N'  # only 'O' is added in queue
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in dirs:
                if nr < 0 or nc < 0 or nr >= nrow or nc >= ncol or (nr, nc) in visited:
                    continue
                if board[nr][nc] == 'O':
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        for i in range(0, nrow):
            for j in range(0, ncol):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'N':
                    board[i][j] = 'O'


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        visited = set()
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    queue = [(i, j)]
                    switch = True
                    switchSet = set(queue)
                    while queue:
                        r, c = queue.pop(0)
                        dire = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                        for nr, nc in dire:
                            if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                                continue
                            if (nr, nc) in switchSet:
                                continue
                            if board[nr][nc] == 'O':
                                queue.append((nr, nc))
                                switchSet.add((nr, nc))
                                if nr == 0 or nr == len(board) - 1 or nc == 0 or nc == len(board[0]) - 1:
                                    switch = False
                    if switch == True:
                        for xr, xc in switchSet:
                            board[xr][xc] = 'X'
                    else:
                        visited.update(switchSet)
