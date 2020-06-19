'''
154. Find Minimum in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:
Input: [2,2,2,0,1]
Output: 0
'''


# remove duplicates at the end - then possibilities is rotated, with only equals around start pointer, either larger or smaller, equal
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] < nums[end]:
                # smaller numbers are can be found at least on mid
                end = mid
            else:
                # smaller numbers are can be found at least on end
                start = mid
        return min(nums[start], nums[end])
