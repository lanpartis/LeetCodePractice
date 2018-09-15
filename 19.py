# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1=head
        p2=head
        for i in range(n):
            if p1.next:
                p1=p1.next
            else:
                if i==n-1:
                    return head.next
                else:
                    return head
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        p2.next=p2.next.next
        return head
