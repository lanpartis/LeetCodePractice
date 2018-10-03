# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1=0
        a1=headA
        while a1 is not None:
            a1=a1.next
            l1+=1
        l2=0
        a2=headB
        while a2 is not None:
            a2=a2.next
            l2+=1
        if l1>l2:
            l1,l2=l2,l1
            headA,headB=headB,headA
        for i in range(l2-l1):
            headB=headB.next
        while headA is not None:
            if headA == headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None