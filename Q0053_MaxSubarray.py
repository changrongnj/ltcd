'''
Q53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has
the largest sum and return its sum.


Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Ans: A list to record the max result at current index.
1. res to record final maxSubArray, intialize as the first element in nums
2. while iterate index, the max value at current index will be either current value OR sum of list[index - 1] + current value
3. res keep tracking the max value
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSoFar = [nums[0]]
        res = nums[0]
        for i in range(1, len(nums)):
            maxSoFar.append(max(maxSoFar[i - 1] + nums[i], nums[i]))
            res = max(res, maxSoFar[i])
        return res
