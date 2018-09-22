# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        header = ListNode(None)
        header.next = head
        prev = header
        now = head
        nex = now.next
        while nex!=None:
            #switch
            prev.next = nex
            now.next =nex.next
            nex.next = now
            #move
            prev = now
            now = prev.next
            if now == None:
                break
            nex = now.next
        return header.next
