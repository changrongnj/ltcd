'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        travsl = [[root.val]]
        while q:
            level = []
            levelVal = []
            for node in q:
                if node.left:
                    level.append(node.left)
                    levelVal.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    levelVal.append(node.right.val)
            q = level
            if level != []:
                travsl.append(levelVal)
        return travsl[::-1]
                
            
            
            
                
        