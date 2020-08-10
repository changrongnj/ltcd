'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        sumAtIndex, sums = 0, [0]
        left = -1
        length = float('inf')
        for i in range(len(nums)):
            sumAtIndex += nums[i]
            sums.append(sumAtIndex)
            subSum = sumAtIndex  # from the beginning
            if subSum >= s:
                while subSum - sums[left + 1] >= s and left <= i:
                    left += 1
                length = min(i - (left - 1), length)

        return length if length <= len(nums) else 0
