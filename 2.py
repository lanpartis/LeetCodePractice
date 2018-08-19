# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def add_digit(self,val1,val2,c=0):
        s = (val1+val2+c)%10
        c = int((val1+val2+c)/10)
        return ListNode(s),c

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res_head = ListNode(-1)
        p1 = l1
        p2 = l2
        res_p = res_head
        c=0
        while p1!=None and p2!=None:
            res_p.next,c=self.add_digit(p1.val,p2.val,c)
            p1=p1.next
            p2=p2.next
            res_p=res_p.next
        if p1!=None:
            p=p1
        else:
            p=p2
        while p!=None:
            res_p.next,c=self.add_digit(p.val,0,c)
            p=p.next
            res_p=res_p.next
        if c==1:
            res_p.next=ListNode(1)
        return res_head.next
