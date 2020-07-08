'''
94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''
#M1: recursion - traverse
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node:
            self.helper(node.left)
            self.res.append(node.val)
            self.helper(node.right)

#M2: recursion - d & c
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion - d&c
        return self.helper(root)
        
    def helper(self, node):
        res = []
        if node:
            left = self.helper(node.left)
            right = self.helper(node.right)
            res.extend(left)
            res.append(node.val)
            res.extend(right)
        return res

#M3: Iteration
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, s = [], []
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                return res
            node = s.pop()
            res.append(node.val)
            root = node.right