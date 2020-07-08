'''
Lintcode 597. Subtree with Maximum Average
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.
Example
Given a binary tree:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
return the node 11.
'''
class Tree:
    def __init__(self, root):
        self.root = root
    def __init__(self):
        self.root = None 

    def makeTree(self, input):
        root = TreeNode(input[0])
        self.expandTree(input, root, 0)
        self.root = root
        return root

    def expandTree(self, input, node, i):
        left = i * 2 + 1
        right = i * 2 + 2
        if left > (len(input) - 1) or (right > len(input) - 1):
            return node
        if input[left] is not None:
            leftNode = TreeNode(input[left])
        if input[right] is not None:
            rightNode = TreeNode(input[right])
        node.left = self.expandTree(input, leftNode, left)
        node.right = self.expandTree(input, rightNode, right)
        return node
    
    def traverse(self):
        current_level = [self.root]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            current_level = next_level

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    def __str__(self):
        return str(self.val)

class Solution:

    def MaxSubtreeAverage(self, root):
        self.maxSum = None #(sum, size)
        self.maxSize = 0
        self.maxNode = None
        if root:
            self.maxNode = root
            self.helper(root)
        return self.maxNode
    
    def helper(self, node):
        if not node:
            return (0, 0)
        resLeft = self.helper(node.left)
        resRight = self.helper(node.right)
        subtreeSum = node.val + resLeft[0] + resRight[0]
        subtreeSize = 1 + resLeft[1]+ resRight[1]
        if not self.maxSum or self.maxSum * subtreeSize < subtreeSum * self.maxSize:
            self.maxSum, self.maxSize = subtreeSum, subtreeSize
            self.maxNode = node
        return (subtreeSum, subtreeSize)