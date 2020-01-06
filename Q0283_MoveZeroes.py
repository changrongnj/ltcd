'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Ans key:
1. travel through the list
2. meet 0, if the next one is 0, swap; if not, find next next 0 until last position
swap all th 0 to the end

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                i += 1
            j += 1
        
