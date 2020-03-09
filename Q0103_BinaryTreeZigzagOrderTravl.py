'''
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        v = [root]
        zigzag = [[root.val]]
        odd = 1
        while v:
            level = []
            odd *= -1
            for node in v:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            v = level
            if level:
                zigzag.append([node.val for node in level[::odd]])
            #     if odd == True:
            #         lvlOrder = [node.val for node in level]
            #     else:
            #         lvlOrder = [node.val for node in level[::-1]]
        return zigzag