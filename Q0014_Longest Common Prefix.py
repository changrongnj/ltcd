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

# my answer ...... T.T 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        # shortest string in the strs list
        minLength = len(strs[0])
        word = strs[0]
        for i in range(1, len(strs)):
            if len(strs[i]) < minLength:
                minLength = len(strs[i])
                word = strs[i]
                
        # check all the possibility in a hashtable
        prefix = {}
        for i in range(1, len(word)):
            prefix[word[:i]] = 0
        
        # check if all the strings contain any of this possibilities
        for i in range(len(strs)):
            for ele in prefix:
                if ele in strs[i]:
                    prefix[ele] += 1
        
        # go through the prefix table, if any value larger than len(strs)
        commonPrefix = ""
        for ele, value in prefix.items():
            if value >= len(strs) and len(ele) >= len(commonPrefix):
                commonPrefix = ele
        return commonPrefix