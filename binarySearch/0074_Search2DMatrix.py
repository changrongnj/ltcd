'''
74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        # find row
        up = 0
        down = len(matrix) - 1
        while up + 1 < down:
            mid = up + (down - up) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                up = mid
            else:
                down = mid
        if matrix[down][0] <= target:
            row = down
        else:
            row = up

        # find column
        s = 0
        e = len(matrix[row]) - 1
        while s + 1 < e:
            mid = s + (e - s) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                s = mid
            else:
                e = mid
        if matrix[row][s] == target or matrix[row][e] == target:
            return True
        return False
