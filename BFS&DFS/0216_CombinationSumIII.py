'''
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        self.dfs(1, n, k, [], res)

        return res

    def dfs(self, startNum, target, count, combination, res):
        if count == 0:
            if target == 0:
                res.append(combination)
            return
        for num in range(startNum, 10):
            self.dfs(num + 1, target - num, count -
                     1, combination + [num], res)
