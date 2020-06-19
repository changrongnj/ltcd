'''
81. Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        
        start = 0
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[start]:
                start += 1
            elif nums[mid] < nums[start]:
                if nums[start] <= target:
                    end = mid
                elif nums[start] > target and nums[mid] < target:
                    start = mid
                else: # nums[mid] > target
                    end = mid
            else: # nums[mid] > nums[start]
                if nums[mid] < target:
                    start = mid
                elif nums[mid] > target and target >= nums[start]:
                    end = mid
                else: # nums[mid] > target and target < nums[start]
                    start = mid
        
        if nums[start] == target or nums[end] == target:
            return True
        return False
