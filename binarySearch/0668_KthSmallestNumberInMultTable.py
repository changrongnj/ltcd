'''
668. Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        small = 1
        large = m * n
        while small < large:
            mid = small + (large - small) // 2
            count = 0
            j = n
            for i in range(1, m + 1):
                while j >= 1 and i * j > mid:
                    j -= 1
                count += j
            if count < k:
                small = mid + 1
            else:
                large = mid
        return small
