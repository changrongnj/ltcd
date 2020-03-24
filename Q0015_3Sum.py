'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
# method:
# 1. sort the nums list
# 2. locate first number, find rest two numbers that sum up to 0
# if first number is over 0, break the iteration as it is impossible to get three positive numbers to 0
# 3. left and right two pointers, if the two numbers > remainder （0-firstnumber), move right pointer to left..
# 4. if same, find the right three numbers; but need to continue checking the pointer's next one, if same, skip the duplicate.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:   # reduce duplicates
                continue
            if nums[i] <= 0:  # impossible to have three positive nums add up to 0
                twoOthers = 0 - nums[i]
                left = i + 1
                right = len(nums) - 1
                while left < right: 
                    if nums[left] + nums[right] < twoOthers:  # move left pointer right, as the result is smaller than 0
                        left += 1
                    elif nums[left] + nums[right] > twoOthers: # move right pointer left, as the result is smaller than 0
                        right -= 1
                    else:
                        res.append([nums[i], nums[left], nums[right]]) # find the three numbers
                        while left < right and nums[left + 1] == nums[left]: # skip if the next twos is the same numbers
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1 # continue to find next two nums
                        right -= 1
        return res
                    