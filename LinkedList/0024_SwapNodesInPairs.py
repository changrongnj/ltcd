'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

# recursion


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        neib = head.next
        neib.next = self.swapPairs(neib.next)
        head.next = neib.next
        neib.next = head

        return neib


# iteration
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head

        while curr and curr.next:
            neib = curr.next  # neighbor in pair
            curr.next = neib.next
            neib.next = curr
            prev.next = neib

            prev = curr
            curr = curr.next

        return dummy.next
