# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        p2 = head
        while p2!=None:
            p=p.next
            p2=p2.next
            if p2 is None:
                return False
            p2=p2.next
            if p2==p:
                return True
        return False
            