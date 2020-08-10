'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        nmprev, nm = dummy, head
        # find m and n
        for i in range(1, n):
            if i == m - 1:  # the node before mth node
                nmprev, nm = head, head.next
            head = head.next
        nn, nnplus = head, head.next

        # reverse
        prev, curr = None, nm
        while curr != nnplus:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # connect
        nm.next = nnplus
        nmprev.next = nn

        return dummy.next
