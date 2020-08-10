'''
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []

        if not nums or len(nums) == 0:
            return res

        def dfs(nums, startIndex, subset, res):
            res.append(subset)
            for i in range(startIndex, len(nums)):
                if (i != startIndex and nums[i] == nums[i - 1]):
                    continue
                dfs(nums, i + 1, subset + [nums[i]], res)

        dfs(sorted(nums), 0, [], res)

        return res
