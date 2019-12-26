'''
Q88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

NOTE: in-place merge. 

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - len(nums2) - 1
        j = len(nums2) - 1
        sortLoc = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[sortLoc] = nums1[i]
                i = i - 1
            else:
                nums1[sortLoc] = nums2[j]
                j = j - 1
            sortLoc = sortLoc - 1
        if i < 0 and j >= 0:
            for rest in range(sortLoc + 1):
                nums1[rest] = nums2[rest]
        return nums1
