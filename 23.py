class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists)>2:
            n_lists = list()
            for i in range(0,len(lists),2):
                n_lists.append(lists[i]) if i == len(lists)-1 else n_lists.append(self.merge2Lists(lists[i:i+2]))
            lists = n_lists
        if len(lists)==1:
            return lists[0]
        if len(lists)==0:
            return None
        return self.merge2Lists(lists)


    def merge2Lists(self,lists):
        res=ListNode(None)
        p_res = res
        i=lists[0]
        j=lists[1]
        while i is not None and j is not None:
            if i.val<=j.val:
                p_res.next = i
                p_res=i
                i=i.next
                p_res.next=None
            else:
                p_res.next=j
                p_res=j
                j=j.next
                p_res.next=None
        if i is not None:
            p_res.next = i
        if j is not None:
            p_res.next = j
        return res.next
