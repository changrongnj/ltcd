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
        
        if x < 0:
            return False
        
        res = 0
        num = x
        while num > 0:
            res = res * 10 + num % 10
            num = num // 10
            
        if res != x:
            return False
        
        return True

            
        # method 2:
        """
        1. num to string
        2. string backward read and compare
        """
        xStr = str(x)
        xStrRev = xStr[-1::-1]
        if xStr == xStrRev:
            return True
        return False
  
