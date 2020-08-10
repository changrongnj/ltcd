'''
51. N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []

        res = []
        placed = set()
        self.helper(n, 0, placed, [], res)
        return res

    def helper(self, n, row, placed, placement, res):
        if row == n:
            res.append(placement)
            return

        thisRow = "." * n

        for col in range(n):
            if not self.validQueen(row, col, placed):
                continue
            placed.add((row, col))
            self.helper(n,
                        row + 1,
                        placed,
                        placement + [thisRow[:col] + "Q" + thisRow[col+1:]],
                        res)
            placed.remove((row, col))

    def validQueen(self, i, j, visited):
        for r, c in visited:
            if i == r:
                return False
            if j == c:
                return False
            if abs(r - i) == abs(c - j):
                return False
        return True
