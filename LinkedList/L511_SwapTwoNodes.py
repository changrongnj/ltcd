'''
511. Swap Two Nodes in Linked List

Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. 
It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, 
do nothing.

Example
Example 1:

Input: 1->2->3->4->null, v1 = 2, v2 = 4
Output: 1->4->3->2->null
Example 2:

Input: 1->null, v1 = 2, v2 = 1
Output: 1->null
Notice
You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.
'''


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """

    def swapNodes(self, head, v1, v2):
        if not head or not head.next or v1 == v2:  # 俩个值相同
            return head

        # write your code here
        dummy = ListNode(0)
        dummy.next = head

        n1, n2 = None, None

        prev, curr = dummy, head
        while curr:
            if n1 and n2:
                break
            if curr.val == v1:
                p1, n1 = prev, curr
            if curr.val == v2:
                p2, n2 = prev, curr
            prev, curr = curr, curr.next

        if not n1 or not n2:
            return dummy.next

        # swap n1 and n2
        # 此处顺序不可相反，否则v1,v2相连的case会出问题 10->9->8->7->6->NULL, 10->8->9->7->6->NULL
        p1.next, p2.next = p2.next, p1.next
        n1.next, n2.next = n2.next, n1.next

        return dummy.next
