'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums or len(nums) == 0:
            return []

        res = []
        visited = set()
        self.helper(nums, visited, [], res)

        return res

    def helper(self, nums, visited, permutation, res):
        if len(permutation) == len(nums):
            res.append(permutation)
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            visited.add(i)
            self.helper(nums, visited, permutation + [nums[i]], res)
            visited.remove(i)
