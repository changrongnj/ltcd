'''
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        for num in nums1:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
        res = []
        for num in nums2:
            if num in memo and memo[num] > 0:
                res.append(num)
                memo[num] -= 1
        return res
                