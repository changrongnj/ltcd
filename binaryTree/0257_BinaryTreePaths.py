'''
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# iteration:
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        return paths


# Recursion: divide & conquer
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if left:
            for path in left:
                paths.append(str(root.val) + "->" + path)
        if right:
            for path in right:
                paths.append(str(root.val) + "->" + path)
        return paths

# Recursion: traverse
class Solution:
    res = []
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # recursion - traverse
        self.res = []
        if root:
            self.helper(root, str(root.val))
        return self.res
    
    def helper(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            self.res.append(path)
            return self.res
        if node.left:
            self.helper(node.left, path + "->" + str(node.left.val))
        if node.right:
            self.helper(node.right, path + "->" + str(node.right.val))