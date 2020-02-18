'''
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

# M1: Set, &
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# M2: hash table
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Dict = {}
        for num in nums1:
            if num in nums1Dict:
                nums1Dict[num] += 1
            else:
                nums1Dict[num] = 1
        nums2Dict = {}
        for num in nums2:
            if num in nums2Dict:
                nums2Dict[num] += 1
            else:
                nums2Dict[num] = 1
        res = []
        for num in nums1Dict:
            if num in nums2Dict:
                res.append(num)
        return res
                