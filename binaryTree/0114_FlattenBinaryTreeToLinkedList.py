'''
114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Recursion - divide & conquer
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    def helper(self, node):
        if not node:
            return None
        leftMostLeaf = self.helper(node.left)
        rightMostLeaf = self.helper(node.right)
        if leftMostLeaf:
            leftMostLeaf.right = node.right
            node.right = node.left
            node.left = None
        if rightMostLeaf:
            return rightMostLeaf
        if leftMostLeaf:
            return leftMostLeaf
        return node

# Recursion - traverse
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if root:
            leftSubtree = root.left
            rightSubtree = root.right
            
            self.flatten(leftSubtree)
            self.flatten(rightSubtree)

            root.left = None
            root.right = leftSubtree
            
            currNode = root
            # find the right most leaf through traversal to the most depth
            while currNode.right:
                currNode = currNode.right
            currNode.right = rightSubtree
            currNode.left = None

# iteration
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if stack:
                    node.left = None
                    node.right = stack[-1]
            