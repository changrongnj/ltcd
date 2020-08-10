'''
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

0
[2,6,4]
[1,5]
3
2
-->None
'''


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pt1, pt2 = headA, headB
        # a + c + b =  b + c + a
        while pt1 != pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA

        return pt1
