'''
485. Max Consecutive Ones

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

class Solution:
    """
    Top-down
    """
    dp = {0:0, 1:1}
    def fib(self, N:int) -> int:
        if N not in self.dp:
            self.dp[N] = self.fib(N-1) + self.fib(N-2)
        return self.dp[N]
    """
    Bottom-up
    """
    def fib(self, N: int) -> int:
        dp = {0:0, 1:1}
        for i in range(2,N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]
