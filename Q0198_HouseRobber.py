'''
198. House Robber
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have security system 
connected and it will automatically contact the police if two adjacent houses were broken 
into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Ans: Recursion
1. current rob price = max(val + rob[n - 2]  or rob[n-1])
'''

# M1 - bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = [0, nums[0]]
        for i in range(1, len(nums)):
            memo.append(max(memo[i], memo[i - 1] + nums[i]))
        return memo[-1]