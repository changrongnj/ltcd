'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Ans:
1. Dictionary to store a pair of parenthesis
2. stack
3. careful of empty/not empty: nothing to pop ->first need to check if the stack is able to pop(), also ending with stack == [], not empty meaning not fully pop out.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # store the parathesis
        p = {'(': ')', '[': ']', '{': '}'}
        # #stack first in last out
        v = []
        for char in s:
            if char in p:
                v.append(p[char])
            else:
                if not v or v.pop() != char:
                    return False
        return v == []