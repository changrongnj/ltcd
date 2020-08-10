'''
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        # divide
        left, right = self.divide(head)
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
        
        
    def divide(self, head):

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow
        left = head
        while head != mid:
            head = head.next
        right = head.next
        head.next = None
        
        return left, right
    
    
    def merge(self, head1, head2):
        curr = res = ListNode(0)
        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
            
        if not head1:
            curr.next = head2
        if not head2:
            curr.next = head1
        
        return res.next
        