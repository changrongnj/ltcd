'''
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # build array list
        curr, lst = head, []
        while curr:
            lst.append(curr.val)
            curr = curr.next

        return self.buildBST(lst, 0, len(lst))

    def buildBST(self, nums, s, e):
        if not nums:
            return None
        if s >= e:
            return None
        mid = s + (e - s) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, s, mid)
        root.right = self.buildBST(nums, mid + 1, e)

        return root
