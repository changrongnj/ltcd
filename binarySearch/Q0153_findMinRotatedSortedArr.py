'''
153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
# the last element of the array is either the min or larger than min. Therefore, the target number = nums[end]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        target = nums[end]
        while start + 1 < end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] > target:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])