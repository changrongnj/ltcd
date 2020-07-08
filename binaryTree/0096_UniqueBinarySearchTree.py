'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution:
    
    count_dict = {0:1, 1:1}
    
    def numTrees(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return self.count_dict.get(n)
        count = 0
        
        for i in range(n):
            if i in self.count_dict:
                left = self.count_dict[i]
            else:
                left = self.numTrees(i)
                self.count_dict[i] = left
            if n-i-1 in self.count_dict:
                right = self.count_dict[n - i - 1]
            else:
                right = self.numTrees(n - i - 1)
                self.count_dict[n - i - 1] = right
                
            count += left * right
            
        return count