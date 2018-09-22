class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [x for x in A if x%2==0]
        res.extend([x for x in A if x%2==1])
        return res
