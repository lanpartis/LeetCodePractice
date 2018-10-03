# Definition for singly-linked list.93.7%
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        l=0
        p=head
        while p is not None:
            p=p.next
            l+=1
        p2 = head
        for i in range((l-1)//2):
            p2=p2.next
        p=p2.next
        np=p.next
        p.next=p2
        p2.next = None
        while np is not None:
            t = np.next
            np.next = p
            p = np
            np = t
        h1=head
        h2=p
        for i in range(l//2):
            if h1.val != h2.val:
                return False
            h1=h1.next
            h2=h2.next
        return True

