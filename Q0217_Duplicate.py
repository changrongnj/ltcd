'''
Q217.
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for i in range(len(nums)):
            if nums[i] not in count:
                count.add(nums[i])
            else:
                return True
        return False
