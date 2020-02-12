'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Ans:
1. find the shortest word to work with
2. go through the index and its letter one by one, if every other word with the same index has the same letter, continue,
3. if any word shows different at certain index, stop at the index, return [:index] the index starting different. 
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        # find the word with shortest length
        shortest = strs[0]
        length = len(shortest)
        for i in range(1, len(strs)):
            if len(strs[i]) < length:
                shortest = strs[i]
                
        for index, letter in enumerate(shortest):
            for j in range(len(strs)):
                if strs[j][index] != letter:
                    return shortest[:index]
        return shortest
