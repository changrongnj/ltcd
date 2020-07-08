'''
145. Binary Tree Postorder Traversal
Hard

1682

88

Add to List

Share
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# M1: recursion - traverse
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node:
            self.helper(node.left)
            self.helper(node.right)
            self.res.append(node.val)

# M2: recursion - d & c
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            left = self.postorderTraversal(root.left)
            right = self.postorderTraversal(root.right)
            
            res.extend(left)
            res.extend(right)
            res.append(root.val)
        return res

# M3: iteration
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]