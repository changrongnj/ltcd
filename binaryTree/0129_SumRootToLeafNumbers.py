'''
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''
# recursion: d&c
class Solution:
    def sumNumbers(self, root: TreeNode) -> int: 
        if not root:
            return 0
        return self.helper(root, root.val)
    
    def helper(self, node, numSoFar):
        if not node.left and not node.right:
            return numSoFar
        res = 0
        if node.left:
            res += self.helper(node.left, numSoFar * 10 + node.left.val)
        if node.right:
            res += self.helper(node.right, numSoFar * 10 + node.right.val)
        return res

# iteration
class Solution:
    def sumNumbers(self, root: TreeNode) -> int: 
        res = 0
        if not root:
            return 0
        stack = [(root, root.val)]
        # (node, numSoFar)
        while stack:
            level = stack
            stack = []
            for node, valSoFar in level:
                if node.left:
                    stack.append((node.left, valSoFar * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, valSoFar * 10 + node.right.val))
                if not node.left and not node.right: # the leaf
                    res += valSoFar
        return res