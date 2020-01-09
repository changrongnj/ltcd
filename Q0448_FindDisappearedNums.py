'''
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

class Solution:
    """
    Method 1:
    1. iterate index, the nums[index] represents existing elements of [1,n] in the list
    2. nums[index]-1 represents the exisiting elements shown as the index
    3. mark nums[nums[index]-1] to be negative, therefore, we could iterate the list
    find any positive num in list, and return its index + 1, which is non-existing elements.
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            existEle = abs(nums[i])
            nums[existEle - 1] = - abs(nums[existEle - 1])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    """
    Method 2:
    1. travel the list
    2. nums[i] if not on the right position, e.g., 2 is not on position 1, meaning
    nums[i] != nums[nums[i]-1], then swap it to the right position
    3. if on the right position, move on
    4. scan all the nums in the list, if find nums[i]!=i, meaning that index was missing
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
        ans = []
        for i in range(len(nums)):  
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans
