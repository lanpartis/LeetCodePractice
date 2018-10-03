# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p0 = head
        p1 = head
        p2 = head
        while p2!=None:
            p1 = p1.next
            p2 = p2.next
            if p2==None:
                return None
            p2 = p2.next
            if p1==p2:
                break
        if p2==None:
            return None
        while p0!=p1:
            p0=p0.next
            p1=p1.next
        return p1

