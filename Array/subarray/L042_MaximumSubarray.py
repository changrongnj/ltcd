'''
42. Maximum Subarray II
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

Example
Example 1:
Input:
[1, 3, -1, 2, -1, 2]
Output:
7
Explanation:
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].

Example 2:
Input:
[5,4]
Output:
9
Explanation:
the two subarrays are [5] and [4].
Challenge
Can you do it in time complexity O(n) ?

Notice
The subarray should contain at least one number
'''


class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        if not nums or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        # two pointers
        leftMaxSum = self.maxSumAtEachIndex(nums)
        rightMaxSum = self.maxSumAtEachIndex(nums[::-1])

        maxSum = float('-inf')
        for i in range(len(nums) - 1):
            maxSum = max(
                maxSum, (leftMaxSum[i] + rightMaxSum[len(nums) - i - 1 - 1]))
        return maxSum

    def maxSumAtEachIndex(self, nums):
        maxSum = []
        maxVal, minVal, sumAtIndex = float('-inf'), 0, 0
        for i in range(len(nums)):
            sumAtIndex += nums[i]
            maxVal = max(maxVal, sumAtIndex - minVal)
            maxSum.append(maxVal)
            minVal = min(minVal, sumAtIndex)
        return maxSum
