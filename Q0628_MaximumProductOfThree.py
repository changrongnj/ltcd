'''
628. Maximum Product of Three Numbers

Given an integer array, find three numbers
whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all
elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed
the range of 32-bit signed integer.


Ans:
1. find maximum three
2. because there could be negative, two negative = postive. So,
also find minimum two
3. if 2nd minimum < 0 means both < 0, and check if two minimum * max and three max product

'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        Three = sorted(nums[0:3])
        lgest = Three[2]
        lger = Three[1]
        lg = Three[0]
        smest = Three[0]
        sm = Three[1]
        
        for i in range(3, len(nums)):
            if nums[i] > lgest:
                lgest, lger, lg = nums[i], lgest, lger
            elif nums[i] > lger:
                lger, lg = nums[i], lger
            elif nums[i] > lg:
                lg = nums[i]

            if nums[i] < smest:
                smest, sm = nums[i], smest
            elif nums[i] < sm:
                sm = nums[i]
        posRes = lgest * lger * lg
        if sm < 0:  # meaning smest also < 0
            return max(posRes, lgest * smest * sm)
        return posRes
