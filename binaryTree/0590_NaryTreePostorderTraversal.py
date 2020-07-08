'''
590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
'''

# M1: Recursion
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.helper(root)
        
    def helper(self, node):
        res = []
        if node:
            for child in node.children:
                if child:
                    res.extend(self.helper(child))
            res.append(node.val)
        return res
            

# M2: Iteration
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                stack.extend(node.children)
                res.append(node.val)
        return res[::-1]