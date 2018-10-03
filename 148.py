
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l =0
        p=head
        while p is not None:
            p=p.next
            l+=1
        res = self.mergesort(head,l)
        return res
    
    def mergesort(self,head,length):
        if length<=1:
            return head
        if length==2:
            p1 = head
            p2 = head.next
            if p1.val <= p2.val:
                return head
            else:
                p2.next=p1
                p1.next=None
                return p2
        l1=head
        p=head
        for i in range(length//2-1):
            p=p.next
        l2 = p.next
        p.next=None
        l1 = self.mergesort(l1,length//2)
        l2 = self.mergesort(l2,length-length//2)
        h = ListNode(0)
        p=h
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
            p.next = None
        if l1 is not None:
            p.next = l1
        else:
            p.next = l2
        return h.next
        