class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        cand=list()
        for i in s:
            cand.append(v[i])
        for i in range(len(s)-1):
            if cand[i]<cand[i+1]:
                cand[i]*=-1
        return sum(cand)
