class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        com = ''
        if len(strs)==0:
            return ''
        l = len(strs[0])
        for i in range(l):
            head = strs[0][i]
            b=False
            for s in strs:
                if i>=len(s) or s[i] !=head:
                    b=True
                    break
            if b:
                break
            com+=head
        return com
