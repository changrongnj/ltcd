'''
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        if not nums or len(nums) == 0:
            return res

        def dfs(nums, startIndex, subset, res):
            res.append(subset)
            for i in range(startIndex, len(nums)):
                # '+' = append and create a new ref
                dfs(nums, i + 1, subset + [nums[i]], res)

        dfs(nums, 0, [], res)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)

        if not nums or n == 0:
            return res

        for i in range(1 << n):  # 000 - 111 ->1000 is the upbound
            subset = []
            for j in range(n):
                if (i & 1 << j != 0):  # digit has 1, represent a combination
                    subset.append(nums[j])
            res.append(subset)

        return res
