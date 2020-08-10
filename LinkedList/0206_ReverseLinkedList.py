'''
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
            
        curr, prev = head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev


# recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
            
        def helper(node, prev):
            if not node:
                return prev
            nxt = node.next
            node.next = prev
            return helper(nxt, node)

        return helper(head, None)