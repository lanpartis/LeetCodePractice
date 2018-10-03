class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        table = [False]*len(s)
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if (j==0 or table[j-1])and s[j:i+1] in wordDict:
                    table[i]=True
                    break
        return table[-1]

