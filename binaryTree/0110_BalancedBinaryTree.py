'''
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1
    
    def helper(self, root):
        # return -1 means not balanced
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1