'''
Q9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # method 1: 
        1. %10 push to reversed x
        2. //10 pop out the last digit in x
        3. TO BE NOTE: x changed in push and pop, need to store another x to compare with the reversed x
        """
        xStr = str(x)
        xRevStr = xStr[-1::-1]
        if xStr == xRevStr:
            return True
        else:
            return False
        """
            
        # method 2:
        """
        1. num to string
        2. string backward read and compare
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            xOrig = x
            xRev = 0
            while x != 0:
                xRev = xRev * 10 + x % 10
                x = x // 10
            if xRev == xOrig:
                return True
            else:
                return False