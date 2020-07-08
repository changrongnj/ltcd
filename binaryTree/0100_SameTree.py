'''
100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


Ans:
1. if both are not none, return recursively val && leftsubtree && rightsubtree comparison
2. else only need to compare if p is q.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#M1 iteration
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            np, nq = stack.pop()
            if not np and not nq:
                continue
            if np and nq and np.val == nq.val:
                stack.append((np.left, nq.left))
                stack.append((np.right, nq.right))
            else:
                return False
        return True

#M2 recursion d&c
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p:
            return not q
        if not q:
            return not p
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
