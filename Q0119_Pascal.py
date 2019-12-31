'''
Q119. Pascal's Triangle
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1], [1, 1]]
        if rowIndex > 1: #0:[1], 1:[1,1], 2:[1,2,1]
            i = 2
            while i <= rowIndex:
                row = [1] * (rowIndex + 1)
                for numIndex in range(1, i):  #ith row has index till i
                    row[numIndex] = pascal[i - 1][numIndex - 1] + pascal[i - 1][numIndex]
                pascal.append(row)
                i = i + 1
        return pascal[rowIndex]
