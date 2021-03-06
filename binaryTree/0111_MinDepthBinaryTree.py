'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


#M2. BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:      
        if not root:
            return 0
        depth, stack = 0, [root]
        while stack:
            level = stack
            stack = []
            depth += 1
            for node in level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)