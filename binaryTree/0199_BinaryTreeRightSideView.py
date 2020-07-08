'''
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        if root:
            res.append(root.val)
            right = self.rightSideView(root.right)
            left = self.rightSideView(root.left)
            res.extend(right)
            if len(right) < len(left):
                res.extend(left[len(right):])
        return res

#iteration
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append(level[-1].val)
            #BFS:
            stack = level
            level = []
            for node in stack:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return res