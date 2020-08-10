'''
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                data.append('#')
            else:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        if not vals:
            return None

        root = None
        rootVal = vals.pop(0)
        if rootVal == '#':
            return None
        root = TreeNode(int(rootVal))
        queue = [root]
        while vals:
            parent = queue.pop(0)
            left = vals.pop(0)
            if left != '#':
                parent.left = TreeNode(int(left))
                queue.append(parent.left)
            if vals:
                right = vals.pop(0)
                if right != '#':
                    parent.right = TreeNode(int(right))
                    queue.append(parent.right)
        return root


# DFS
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []

        def preorder(root):
            if not root:
                data.append('#')
            else:
                data.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(','))

        def build():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
