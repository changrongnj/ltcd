'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

# M1: two binary search, find first position and find last position

class Solution:    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[len(nums) - 1] < target:
            return [-1, -1]
        
        first = self.searchFirst(nums, target)
        last = self.searchLast(nums, target)
        if first == -1:
            return [last, last]
        if last == -1:
            return [first, first]
        return [first, last]
    
    
    def searchFirst(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
    
    def searchLast(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1

    

# M2:  find the duplicate sub-array
# 1. stop condition is not index but the num value.  As it is the sorted array, ends if the nums[start] == nums[end]
# 2. if the nums[mid] == target, if nums[start] == target as nums[start] < nums[end], then decrease end pointer; else, increase start pointer
# 3. if the start value == end value == target, find start and end

class Solution:    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        start = 0
        end = len(nums) - 1
        
        while start < end and nums[start] < nums[end]:
            mid = math.floor((start + end) / 2)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else: #mid == target
                if nums[start] == target:
                    end -= 1
                else:
                    start += 1
        
        if nums[start] == target and nums[start] == nums[end]:
            return [start, end]
        return [-1, -1]
