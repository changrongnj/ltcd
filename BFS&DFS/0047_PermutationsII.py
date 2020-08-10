'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if not nums or len(nums) == 0:
            return []

        res = []
        visited = set()
        self.helper(sorted(nums), visited, [], res)
        return res

    def helper(self, nums, visited, permutation, res):
        if len(permutation) == len(nums):
            res.append(permutation)
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            if i != 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
                continue
            visited.add(i)
            self.helper(nums, visited, permutation + [nums[i]], res)
            visited.remove(i)
