'''
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# RECURSION - divde & conquer#
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# RECURSION - TRAVERSE #
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth = 0
        self.helper(root, 1)
        return self.depth
    
    def helper(self, node, thisDepth):
        if not node:
            return
        if self.depth < thisDepth:
            self.depth = thisDepth
        self.helper(node.left, thisDepth + 1)
        self.helper(node.right, thisDepth + 1) 
            

# ITERATION #
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            stack = [root]
            while stack:
                level = stack
                stack = []
                depth += 1
                for node in level:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
        return depth
        
