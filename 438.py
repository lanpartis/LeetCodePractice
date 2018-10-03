#89.76%
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return list()
        h = 0
        t = len(p)-1
        count=0
        res = list()
        pdic=dict()
        sdic=dict()
        for c in p:
            pdic[c]=pdic.get(c,0)+1
            sdic[c]=0
        for c in s[:len(p)]:
            if c in p:
                sdic[c]+=1
                if sdic[c]<=pdic[c]:
                    count+=1
        while True:
            if count ==len(p):
                res.append(h)
            if t==len(s)-1:
                break
            if sdic.get(s[h],None) is not None:
                sdic[s[h]]-=1
                if sdic[s[h]]<pdic[s[h]]:
                    count-=1
            h+=1
            t+=1
            if sdic.get(s[t],None) is not None:
                sdic[s[t]]+=1
                if sdic[s[t]]<=pdic[s[t]]:
                    count+=1
        return res

