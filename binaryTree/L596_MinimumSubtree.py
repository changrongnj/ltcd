'''
Lintcode 596. Minimum Subtree
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
Example
Example 1:
Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:
Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
'''

class Solution:
    #minNode = None
    #minSum = 0
    def findMinHeight(self, root):
        self.minNode = None
        self.minSum = 0
        if root:
            self.minNode = root
            self.helper(root)
        return self.minNode

    def helper(self, node):
        if not node:
            return
        subtreeSum = node.val + self.helper(node.left) + self.helper(node.right) 
        if subtreeSum < self.minSum:
            self.minSum = subtreeSum
            self.minNode = node

