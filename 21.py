# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next =l1
                l1 = l1.next
                p = p.next
                p.next = None
            else:
                p.next =l2
                l2 = l2.next
                p = p.next
                p.next = None
        if l1 is not None:
            p.next = l1
        else:
            p.next = l2
        return head.next
