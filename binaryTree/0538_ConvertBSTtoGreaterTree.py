'''
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
'''

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        add = 0
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.right
            if not stack:
                return root
            node = stack.pop()
            node.val += add
            add = node.val
            node = node.left


 class Solution:
    add = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            root.val += self.add
            self.add = root.val
            self.convertBST(root.left)
        return root


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        total = left + right + root.val

        root.val += right
        stack = [root.left]
        while stack:
            level = stack
            stack = []
            for node in level:
                if node:
                    node.val += root.val
                    stack.append(node.left)
                    stack.append(node.right)

        return total
