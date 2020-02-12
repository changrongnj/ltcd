'''
Q53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has
the largest sum and return its sum.


Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


NOTE: dp record the max of every subarray ending with index travel 0 - lens(nums)
'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            maxEndAtIndex = [nums[0]]
            maxVal = maxEndAtIndex[0]
            for i in range(1, len(nums)):
                maxEndAtIndex.append(max(maxEndAtIndex[i - 1] + nums[i], nums[i]))
                # max of (sum of previous max ending with index i - 1) or (single element ith)
                maxVal = max(maxVal, maxEndAtIndex[i])
                # update the max value after new dp[i] recorded
            return maxVal
