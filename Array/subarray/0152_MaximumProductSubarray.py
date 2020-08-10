'''
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0:
            return 0

        maxp = minp = 1
        res = float('-inf')
        for num in nums:
            x = max(num, maxp * num, minp * num)
            y = min(num, maxp * num, minp * num)
            maxp, minp = x, y
            res = max(res, maxp)
        return res
