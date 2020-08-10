'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates or len(candidates) == 0:
            return

        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res

    def dfs(self, nums, target, startIndex, combination, res):
        if target == 0:
            res.append(combination)
            return
        for i in range(startIndex, len(nums)):
            if nums[i] > target:
                return
            if i != startIndex and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, target - nums[i], i +
                     1, combination + [nums[i]], res)
