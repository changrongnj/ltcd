'''
628. Maximum Product of Three Numbers
Given an integer array, find three numbers whose
product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements
are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range
of 32-bit signed integer.


Ans:
Note, small and large cannot be at the same array
1. initialize smallest and largest value from nums[0] subarray; initialize maxDis = 0
2. travel the list-nums: update maxDis with new stored largest(not in same subarray with new one) - subarray[0]
and new subarray[end] - stored smallest

'''

Class Solution:
    def maximumDistanceInArray(self, nums: List[list[int]]) -> int:
        smNum = nums[0][0]
        lgNum = nums[0][len(nums[0]) - 1]
        maxDis = 0
        for i in range(1, len(nums)):
            maxDis = max(maxDis, lgNum - nums[i][0], nums[i][len(nums[i]) - 1] - smNum)
            smNum = min(smNum, nums[i][0])
            lgNum = max(lgNum, nums[i][len(nums[i]) - 1])
            
        return maxDis
