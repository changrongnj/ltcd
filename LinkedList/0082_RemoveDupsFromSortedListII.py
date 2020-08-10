'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head

        while curr and curr.next:
            if prev.next.val != curr.next.val:
                prev, curr = curr, curr.next
            else:
                while curr.next and prev.next.val == curr.next.val:
                    curr = curr.next
                curr = curr.next
                prev.next = curr

        return dummy.next
