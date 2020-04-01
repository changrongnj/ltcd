'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
#two pointers

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        rtn = sum(nums[:3])  #initialize the first three elements as the final sum result
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == target:
                    return target
                
                if abs(target - threeSum) < abs(target - rtn):
                        rtn = threeSum
                
                if threeSum < target:
                    l += 1
                if threeSum > target:
                    r -= 1
        return rtn