'''
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

#M1 - two pointers - slower and quicker

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = j = len(s) - 1
        while j >= 0 and i >= 0:
            if s[j] != " ":
                i = j
                while i >= 0:
                    if s[i] == " ":
                        return j - i
                    i -= 1
                return j - i
            j -= 1
        return 0


# M2 - String.split()

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if len(s.split()) == 0 else len(s.split()[-1])