class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo={}
        def match(i,j):
            if (i,j) not in memo:
                if j == len(p):
                    ans = i==len(s)
                else:
                    if i<len(s) and p[j] in {s[i],'.'}:
                        if j<len(p)-1 and p[j+1] =='*':
                            ans = match(i+1,j) or match(i+1,j+2) or match(i,j+2)
                        else:
                            ans = match(i+1,j+1)
                    elif j<len(p)-1 and p[j+1] =='*':
                        ans = match(i,j+2)
                    else:
                        ans = False
                memo[i,j]=ans
            return memo[i,j]
        return match(0,0)
