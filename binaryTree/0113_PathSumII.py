'''
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# recursion: d&c
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        if not root.left and not root.right:
            if sum == root.val:
                return [[root.val]]
        
        left, right = [], []
        if root.left:
            left = self.pathSum(root.left, sum - root.val)
        if root.right: 
            right = self.pathSum(root.right, sum - root.val)
        
        total = left + right

# recursion: traverse
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.paths = []
        self.helper(root, [], sum)
        return self.paths
    
    def helper(self, node, path, valInNeed):
        if node:
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == valInNeed:
                    self.paths.append(path)
            if node.left:
                path1 = list(path)
                self.helper(node.left, path1, (valInNeed - node.val))
            if node.right:
                path2 = list(path)
                self.helper(node.right, path2, (valInNeed - node.val))      