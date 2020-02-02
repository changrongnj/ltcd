'''
101. Symmetric Tree


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Ans:
Recursively:
def isMirror() that take left and right as two parameters, everytime
recursively call left.val == right.val, isMirror(left.left, right.right),
and isMirror(left.right, right.left), until left and right either one is None or both


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# RECURSION #

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, l, r):
        if l and r:
            return l.val == r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)
        return l == r


# ITERATION #

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = [(root.left, root.right)]
        while queue:
            l, r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        return True
                
            
