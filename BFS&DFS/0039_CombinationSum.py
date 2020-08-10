'''
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 
Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates:
            return []

        res = []

        self.dfs(sorted(candidates), target, 0, [], res)

        return res

    def dfs(self, candidates, target, start, combination, res):
        if target == 0:
            res.append(combination)

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.dfs(candidates, target -
                     candidates[i], i, combination + [candidates[i]], res)



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if not candidates:
            return []
        
        res = []
        
        self.dfs(sorted(candidates), target, 0, [], res)
        
        return res
    
    
    def dfs(self, candidates, target, start, combination, res):
        if target == 0:
            res.append(list(combination))
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            
            combination.append(candidates[i])
            
            self.dfs(candidates, target - candidates[i], i, combination, res)
            
            combination.pop()