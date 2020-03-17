'''
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# M1: count for the length of two lists, and start one list first till they meet together
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        PtA = headA
        counterA = 1
        while PtA.next != None:
            PtA = PtA.next
            counterA += 1
        PtB = headB
        counterB = 1
        while PtB.next != None:
            PtB = PtB.next
            counterB += 1
        diff = abs(counterA - counterB)  # length difference between A and B
        
        PtA = headA
        PtB = headB
        for i in range(diff):
            if counterA >= counterB:
                PtA = PtA.next
            else:
                PtB = PtB.next
        while PtA != PtB:
            PtA = PtA.next
            PtB = PtB.next
        return PtA

# M2: A + C + B = B + C + A 2nd iteration will meet at the C1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        PtA, PtB = headA, headB
        while PtA != PtB:
            PtA = headB if not PtA else PtA.next 
            PtB = headA if not PtB else PtB.next
            #PtA = PtA.next if PtA.next else headB
            #PtB = PtB.next if PtB.next else headA
        return PtA