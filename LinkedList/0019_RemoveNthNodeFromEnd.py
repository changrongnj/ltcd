'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # find length
        length = 0
        curr = dummy
        while curr.next:
            curr = curr.next
            length += 1

        if n == length:
            return head.next

        k = length - n % length
        # find the one to be removed
        prev, curr = dummy, head
        while k > 0:
            prev, curr = curr, curr.next
            k -= 1

        prev.next = curr.next
        curr.next = None

        return dummy.next
