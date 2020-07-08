'''
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22
'''
# Recursion
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# Iteration
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, sumSoFar = stack.pop()
            if not node.left and not node.right:
                if sumSoFar == sum:
                    return True
                else:
                    continue
            if node.left:
                stack.append((node.left, sumSoFar + node.left.val))
            if node.right:
                stack.append((node.right, sumSoFar + node.right.val))
        return False