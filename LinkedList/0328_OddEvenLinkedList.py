'''
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        odd = ho = ListNode(0)
        even = he = ListNode(0)

        flag = True
        while head:
            if flag:
                odd.next = head
                odd = odd.next
            if not flag:
                even.next = head
                even = even.next
            flag = not flag
            head = head.next

        odd.next = he.next
        even.next = None

        return ho.next
