'''
144. Binary Tree Preorder Traversal
'''
# M1. recursion - traverse
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion - traverse
        self.res = []
        self.helper(root)
        return self.res
        
    def helper(self, node):
    # void return
        if node:
            self.res.append(node.val)
            self.helper(node.left)
            self.helper(node.right)


# M2. recursion - divide & conquer
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursion - divide & conquer
        
        result = []
        if root:
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
            result.append(root.val)
            result.extend(left)
            result.extend(right)
        return result


# M3. iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #iterative
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result