'''
99. Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
'''


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            err1, err2 = None, None
            stack = []
            node = root
            orderPath = []
            while True:
                while node:
                    stack.append(node)
                    node = node.left
                if not stack:
                    break
                node = stack.pop()
                if orderPath and node.val < orderPath[-1].val:
                    if not err1:
                        err1 = orderPath[-1]
                    err2 = node
                orderPath.append(node)
                node = node.right

        err1.val, err2.val = err2.val, err1.val
