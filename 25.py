class Solution(object):

    def reverse_k(self,p_list_head,k):#len(p)>=2
        t_head =p_list_head
        t_tail = p_list_head.next
        tail=None
        p = t_head.next
        n_head = p.next
        p.next = tail
        for i in range(k-1):
            tail = p
            p = n_head
            n_head = n_head.next
            p.next = tail
        p.next = tail
        t_tail.next = n_head
        t_head.next =p
        return t_tail

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Definition for singly-linked list.

        if head == None:
            return None
        if k == 1:
            return head
        header = ListNode(None)
        header.next = head
        p = header
        scanner = p
        end = False
        while True:
            for i in range(k):
                scanner = scanner.next
                if scanner == None:
                    end = True
                    break
            if end:
                break
            scanner = self.reverse_k(p,k)
            p = scanner
        return header.next
