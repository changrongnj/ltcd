'''
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev, curr = head, head.next

        while curr:
            if prev.val != curr.val:
                prev, curr = curr, curr.next
            else:
                while curr and prev.val == curr.val:
                    curr = curr.next
                prev.next = curr

        return dummy.next
