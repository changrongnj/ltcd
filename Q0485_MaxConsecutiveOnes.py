'''
485. Max Consecutive Ones

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
    1. iterate i to travel through the list
    2. if nums[i] is 1, then counter +1,maxOnes to record the max counter till so far
    3. else counter reset to 0, maxOnes to record the max counter till so far

    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOnes = 0
        maxOnes = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                countOnes += 1
            else:
                countOnes = 0
            
            if countOnes > maxOnes:
                maxOnes = countOnes
        return maxOnes
