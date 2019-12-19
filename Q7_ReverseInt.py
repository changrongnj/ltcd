'''
Q7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example:

Input: 123
Output: 321

Input: -123
Output: -321

Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
function returns 0 when the reversed integer overflows.

Note:
Python cannot check using the backward checking
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = abs(x)
        rev = 0
        while (num != 0):
            tail = num % 10
            rev = rev * 10 + tail
            '''  not work in python, check directly within the range
            if (tmp - tail) / 10 != rev:
                return 0
                break
            else:
            '''
            num = num // 10
    
        if x < 0:
            rev = 0 - rev
            
        if rev > (2 ** 31 - 1) or rev < (- 2 ** 31):
            return 0
        else:
            return rev