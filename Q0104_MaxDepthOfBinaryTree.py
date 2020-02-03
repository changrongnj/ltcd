'''
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


Ans:
M1. Recursively: DFS
1. if root is null, return 0
2. if root is not null depth will be 1 +
3. recursively call (maxDepth(root.left))  (maxDepth(root.right))
M2. Iteratively: BFS
1. if root is null return 0
2. depth = 0, level 1 = [root]
3. if root is null. then return depth;
similarly, if level contains null, depth is there
4. while level is not null, adding 1 to depth
keep getting all elements' left and right
queue = [level.each node.left, level.each node.right]
5. when all node in this level finished, level is null, then level = queue,
which is next new level


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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = [root]  # store nodes in every level
        depth = 0
        while level:
            depth += 1
            queue = []  ## store every node's node.left, and node.right
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)        
            # after travel through the level, meaning a next level is fully stored in queue
            level = queue
        return depth
        
