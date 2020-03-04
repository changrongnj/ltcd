'''
67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

#M1 - iterative
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        
        # make up 0 till lengths of two string are the same
        if len(a) >= len(b):
            b = "0" * (len(a) - len(b)) + b
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        
        i = len(a) - 1
        carry = 0
        out = ""
        while i >= 0: #backtravesal till the first element, index is n
            res = int(a[i]) + int(b[i]) + carry
            if res < 2:
                carry = 0
                out = str(res) + out
            else:
                carry = 1
                out = str(res - 2) + out
            i-= 1
        if carry == 1:
            out = "1" + out
        return out

# M2 - recursive
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'