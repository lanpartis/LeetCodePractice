class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m_dic = dict()
        c_dic = dict()
        count = 0
        start = 0
        end = -1
        ms,me=0,len(s)
        for c in t:
            m_dic[c] = m_dic.get(c,0)+1
            c_dic[c] = 0
        while start!=len(s):
            if count<len(t):
                end+=1
                if end==len(s):
                    break
                if s[end] in t:
                    if c_dic[s[end]]<m_dic[s[end]]:
                        count+=1
                    c_dic[s[end]]+=1
            
            if count==len(t):
                if end-start<me-ms:
                    me,ms=end,start
                if s[start] in t:
                    c_dic[s[start]]-=1
                    if c_dic[s[start]]<m_dic[s[start]]:
                        count-=1
                start+=1
        if me == len(s):
            return ""
        return s[ms:me+1]

