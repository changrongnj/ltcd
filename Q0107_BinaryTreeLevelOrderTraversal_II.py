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
            for node in q:
                l, r = node.left, node.right
                if not l and not r:
                    continue
                elif not l:
                    level.append(r)
                elif not r:
                    level.append(l)
                else:
                    level.append(l)
                    level.append(r)
            q = level
            if level != []:
                travsl.append(node.val for node in level)
        return travsl[::-1]
                
            
            
            
                
        