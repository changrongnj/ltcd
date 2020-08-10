'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        if not s or len(s) == 0:
            return []

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, myStr, subStrs, res):
        if myStr == "":
            res.append(subStrs)
            return

        for i in range(1, len(myStr) + 1):
            if not self.isPalindrome(myStr[:i]):
                continue
            self.dfs(myStr[i:], subStrs + [myStr[:i]], res)

    def isPalindrome(self, myStr):
        if myStr == myStr[::-1]:
            return True
        return False
