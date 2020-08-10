'''
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head or not head.next:
            return True

        # find middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h1, h2 = head, None
        tmp = slow.next
        slow.next = None

        # reverse second half
        while tmp:
            nxt = tmp.next
            tmp.next = h2
            h2 = tmp
            tmp = nxt

        while h2:  # h1 length > h2
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next

        return True
