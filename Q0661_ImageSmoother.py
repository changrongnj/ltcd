'''
661. Image Smoother

Given a 2D integer matrix M representing the gray scale of an image,
you need to design a smoother to make the gray scale of each cell becomes
the average gray scale (rounding down) of all the 8 surrounding cells and
itself. If a cell has less than 8 surrounding cells, then use as many as
you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0


Ans:
Straightforward to add surrounding elements together, if over index, not do anything
1. iterate through list of list, for row := 0 - nrows and col := 0 - ncols
2. set up a counter to calculate how many elements added up
3. go through the surrounding 9 elements: for nearRow := row-1,row,row+1  for nearCol:=col-1, col, col+1
4. condition: nearRow within 0 - totalRow, nearCol within 0 - totalCol
5. ans[row][col] += M[nearRow][nearCol] and divides by counter.

'''

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        totalRow, totalCol = len(M), len(M[0])
        ans = []
        for row in range(totalRow):
            ans.append([0] * totalCol)
            
        for row in range(totalRow):
            for col in range(totalCol):
                counter = 0
                for nearRow in range(row - 1, row + 2):  # row-1, row, row+1
                    for nearCol in range(col - 1, col + 2):  # col-1, col, col+1
                        if 0 <= nearRow < totalRow and 0 <= nearCol < totalCol:
                            counter += 1
                            ans[row][col] += M[nearRow][nearCol]
                ans[row][col] = math.floor(ans[row][col] / counter)
        
        return ans
