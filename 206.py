# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # # recursive method
        # h = head
        # t = head.next
        # t = self.reverseList(t)
        # p = t
        # while p.next is not None:
        #     p=p.next
        # p.next = h
        # h.next = None
        # return t
        
        #iterative method
        h = head
        p = h.next
        h.next = None
        while p.next is not None:
            n_p=p.next
            p.next = h
            h = p
            p = n_p
        p.next = h
        return p
        
        
        