'''
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
'''


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.traversal(root)
        return self.res

    def traversal(self, root):
        if root:
            self.traversal(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            self.traversal(root.right)


# iteration: inorder traversal
# instead of return trigger of empty stack, reduce k if k is not 0, until return node.val when k == 0
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        inorder = []
        node, stack = root, []
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            inorder.append(node.val)
            node = node.right
