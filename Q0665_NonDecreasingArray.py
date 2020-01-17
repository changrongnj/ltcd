'''
665. Non-decreasing Array

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].

Ans:
1. flip variable to record if flip is been used once
2. check nums[i-1] and nums[i-2]:
if nums[i-1] > nums[i], meaning need to flip. flip + 1; How to flip?
3. if i - 2 不存在 or i - 2 < i, meaning we could use nums[i] for nums[i-1]; thus, nums[i-1] = nums[i]
4. if nums[i-2] >= nums[i], meaning nums[i] need to be nums [i-1] in order larger or equals to nums[i-2]

'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flip = 0
        if len(nums) > 2:
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    flip += 1
                    if flip > 1:
                        return False
                    if i - 2 < 0 or nums[i - 2] < nums[i]: 
                        nums[i - 1] = nums[i]
                    else:
                        nums[i] = nums[i - 1]
        return True    
