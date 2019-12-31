'''
Q26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


Ans idea:
(Python)
1. two pointers
2. array in-place swap the duplicates with the next num first 
   appearance (put all the identical nums at the beginning and throw duplicates at the end).
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = i + 1
        while i < len(nums) and j < len(nums):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
            j = j + 1
        length = i + 1      
        return length