'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and c
onquer approach, which is more subtle.
'''


# maximum sum till each index, the next one will be either itself max sum till previous index + self
# record maxSumAtIndex and maxSUm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        maxAtIndex = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            maxAtIndex = max(maxAtIndex + nums[i], nums[i])
            maxSum = max(maxSum, maxAtIndex)
        return maxSum


# prefix sum, sum to record sum till current index, maxSum should be current sum - minSumBefore,
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        maxSum = float('-inf')
        sumAtIndex, minSumBefore = 0, 0  # minus nothing, subarray starts with 0

        for i in range(len(nums)):
            sumAtIndex += nums[i]
            maxSum = max(sumAtIndex - minSumBefore, maxSum)
            minSumBefore = min(sumAtIndex, minSumBefore)

        return maxSum
