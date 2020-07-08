'''
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
'''

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))
    
    def helper(self, node):
        if not node:
            return 0, 0
        
        leftRob, leftNotRob = self.helper(node.left)
        rightRob, rightNotRob = self.helper(node.right)
        
        nodeRob = leftNotRob + rightNotRob + node.val
        nodeNotRob = max(leftRob, leftNotRob) + max(rightRob, rightNotRob)
        
        return nodeRob, nodeNotRob