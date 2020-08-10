'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        head = dummy

        while head:
            head = self.reverseNextK(head, k)

        return dummy.next

    def reverseNextK(self, head, k):
        # find k
        n1, nk = head.next, head

        while k > 0:
            nk = nk.next
            k -= 1
            if not nk:
                return None

        nkplus = nk.next

        # reverse
        prev, curr = None, n1
        while curr != nkplus:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # connect
        n1.next = nkplus
        head.next = nk

        return n1
