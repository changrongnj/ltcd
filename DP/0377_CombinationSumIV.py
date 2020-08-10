'''
377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [1] + [0 for _ in range(target)]
        nums = sorted(nums)

        for value in range(1, target + 1):
            for num in nums:
                if num > value:
                    break
                elif num == value:
                    dp[value] += 1
                else:
                    dp[value] += dp[value - num]

        return dp[-1]
