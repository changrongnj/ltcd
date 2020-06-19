'''
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = math.floor(start + (end - start) / 2)
            if mid % 2 == 0:
                if nums[mid - 1] == nums[mid]:
                    end = mid
                else:
                    start = mid
            else: #mid % 2 == 1
                if nums[mid - 1] == nums[mid]:
                    start = mid
                else:
                    end = mid
        #only start and end left
        if start == 0:
            return nums[start]
        else:
            if nums[start - 1] == nums[start]:
                return nums[end]
            else:
                return nums[start]