class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxl=0
        locale=0
        for i in range(len(s)*2-1):
            l = search(s,i)
            if maxl <l:
                maxl = l
                locale=i
        if locale %2 == 1:
            res = s[locale//2-maxl//2+1:locale//2+maxl//2+1]
        else:
            res = s[locale//2-maxl//2:locale//2+maxl//2+1]
        return res
def search(s,i):
    if i%2==1:
        l=0
        i = i//2
        for j in range(0,min(i,len(s)-i-2)+1):
            if s[i-j]==s[i+1+j]:
                l+=2
            else:
                break
    else:
        l = 1
        i = i//2
        for j in range(1,min(i,len(s)-i-1)+1):
            if s[i-j]==s[i+j]:
                l+=2
            else:
                break
    return l
