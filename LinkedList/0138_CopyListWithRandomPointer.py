'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
'''


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        copyDict = dict()
        curr = head
        while curr:
            copyDict[curr] = Node(curr.val)
            curr = curr.next

        for rawNode in copyDict:
            if rawNode.next:
                copyDict[rawNode].next = copyDict[rawNode.next]
            if rawNode.random:
                copyDict[rawNode].random = copyDict[rawNode.random]

        return copyDict[head]


# inplace

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        self.copyList(head)
        self.copyRandomPointer(head)
        return self.splitList(head)

    '''
    7->13->11->10->1->None
    7->7'->13->13'->11->11'->10->10'->1->1'->None
    '''

    def copyList(self, head):
        if not head:
            return None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt

    def copyRandomPointer(self, head):
        if not head:
            return None
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

    '''
    7->7'->13->13'->11->11'->10->10'->1->1'->None
    7'->13'->11'->10'->1'->None
    '''

    def splitList(self, head):
        if not head:
            return None, None
        newHead = newCurr = Node(0)
        while head:
            newCurr.next = head.next
            head = head.next.next
            newCurr = newCurr.next
        return newHead.next
