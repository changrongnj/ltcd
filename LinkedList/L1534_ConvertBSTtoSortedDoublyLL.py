'''
Convert a BST to a sorted circular doubly-linked list in-place. 
Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

Example
Example 1:

Input: {4,2,5,1,3}
        4
       /  \
      2   5
     / \
    1   3
Output: "left:1->5->4->3->2  right:1->2->3->4->5"
Explanation:
Left: reverse output
Right: positive sequence output
Example 2:

Input: {2,1,3}
        2
       /  \
      1   3
Output: "left:1->3->2  right:1->2->3"
'''


class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def treeToDoublyList(self, root):
        head, tail = self.helper(root)
        tail.right = head
        head.left = tail
        return head

    '''
    return head + tail
    '''

    def helper(self, root):

        if not root:
            return

        hl, tl = root, root
        hr, tr = root, root

        if root.left:
            hl, tl = self.helper(root.left)
            tl.right = root
            root.left = tl

        if root.right:
            hr, tr = self.helper(root.right)
            root.right = hr
            hr.left = root

        return hl, tr
