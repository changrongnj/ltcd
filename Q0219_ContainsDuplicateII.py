'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        kVisit = set()
        for i in range(len(nums)):
            if nums[i] not in kVisit:
                kVisit.add(nums[i])
                if i >= k:
                    kVisit.remove(nums[i - k])
            else:
                return True
        return False
