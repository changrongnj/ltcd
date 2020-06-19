'''
378. Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        small = matrix[0][0]
        large = matrix[n-1][n-1]
        while small < large:
            count = 0
            mid = small + (large - small) // 2
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            if count < k:
                small = mid + 1
            else:
                large = mid
        return small
'''
If the mid variable converges to an integer, a_mid, which is not the kth smallest element, a_k, in the array.
Then, a_mid should be bigger than a_k, if not the count will be less than k and a_mid will increase.
Therefore, lo<=a_k<a_mid<=hi will be true, and the loop ends at lo=hi, which means a_mid has to equal to a_k.

Looks like a squeeze theorem.
'''