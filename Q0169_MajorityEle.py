'''
Q169. Majority Elements
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return none
        elif len(nums) == 1:
            return nums[0]
        else:
            occurence = {}
            for i in range(len(nums)):
                if nums[i] in occurence:
                    occurence[nums[i]] += 1
                else:
                    occurence[nums[i]] = 1
                if occurence[nums[i]] > math.floor(len(nums) / 2):
                    return nums[i]