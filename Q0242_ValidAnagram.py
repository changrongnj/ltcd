'''
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Ans:
hash table
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        memo = {}
        for char in s:
            if char in memo:
                memo[char] += 1
            else:
                memo[char] = 1
        for char in t:
            if char in memo:
                memo[char] -= 1
            else:
                return False
        for value in memo.values():
            if value != 0:
                return False
        return True