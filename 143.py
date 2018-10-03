# Definition for singly-linked list. 72.80%
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None:
            return
        p=head
        l=0
        while p is not None:
            l+=1
            p=p.next
        p = head
        for _ in range((l-1)//2):
            p=p.next
        n_p = p.next
        p.next=None
        while n_p is not None:
            p_ = n_p.next
            n_p.next = p
            p = n_p
            n_p = p_
        p0=head
        h = ListNode(0)
        for _ in range(l//2):
            h.next = p0
            n0 = p0.next
            n1 = p.next
            p0.next=p
            h=p
            p0=n0
            p=n1
        if l%2==1:
            h.next = p0
            p0.next=None
        else:
            h.next=None
        