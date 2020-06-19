'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

# start and mid position

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        start = 0
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else: # nums[start] > nums[mid]
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target:
             return start
        if nums[end] == target:
            return end
        return -1
                    
                
                
            