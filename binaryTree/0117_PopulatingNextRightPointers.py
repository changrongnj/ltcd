'''
117. Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        level = [root]
        while level:
            tmp = level
            level = []
            for i in range(len(tmp)):
                node = tmp[i]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                if i + 1 < len(tmp):
                    node.next = tmp[i + 1]
        return root
        