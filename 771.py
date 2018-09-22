class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        h = dict()
        count = 0
        for j in J:
            h[j] = True
        for s in S:
            if h.get(s,False):
                count+=1
        return count
