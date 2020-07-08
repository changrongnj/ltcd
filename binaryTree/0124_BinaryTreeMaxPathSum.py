'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(self.helper(root))
        
    def helper(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return node.val, node.val
        max_till_node, max_sum = node.val, node.val
        if node.left:
            max_till_left, max_left = self.helper(node.left)
            max_till_node = max(max_till_node, max_till_left + node.val)
            max_sum = max(max_sum, max_left, max_till_node)
        if node.right:
            max_till_right, max_right = self.helper(node.right)
            max_till_node = max(max_till_node, max_till_right + node.val)
            max_sum = max(max_sum, max_right, max_till_node)
        if node.left and node.right:
            cross_left_right = max_till_left + max_till_right + node.val
            max_sum = max(max_sum, cross_left_right)
        return max_till_node, max_sum