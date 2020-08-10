'''
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# iteration
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]
        while level:
            tmp = level
            resLevel, level = [], []
            for node in tmp:
                if node:
                    resLevel.append(node.val)
                    level.append(node.left)
                    level.append(node.right)
            if resLevel: # this check is important, otherwise may return [] with else not node..
                res.append(resLevel)
        return res

# recursion
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.helper(root)
        
    def helper(self, node):
        if not node:
            return []
        
        left = self.helper(node.left)
        right = self.helper(node.right)
       
        res = [[node.val]]
        
        #merge left to right
        minLength = min(len(left), len(right))
        for i in range(minLength):
            if left[i] or right[i]:
                left[i].extend(right[i]) 
                res.append(left[i])
        if len(left) > minLength:
            res.extend(left[minLength:])
        if len(right) > minLength:
            res.extend(right[minLength:])
            
        return res