'''
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # method 1 #
        numsSet = set(nums)
        for num in range(len(nums) + 1):
            # length of non-missing array is len(nums)+1
            # last element is len(nums) + 1 - 1
            # python range end exclusion
            if num not in numsSet:
                return num

        # method 2 # Sum
        withoutMissingSum = (1+len(nums))*len(nums)/2
        withMissingSum = sum(nums)
        return int(withoutMissingSum - withMissingSum)

        # method 3 # XOR
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res
        
