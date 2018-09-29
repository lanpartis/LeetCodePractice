class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0:
            return 0
        nexts = get_next(needle)
        i = 0
        j = 0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
                if j == len(needle):
                    break
            else:
                while j>=0 and haystack[i]!=needle[j]:
                    j = nexts[j]
                i+=1
                j+=1
            if j == len(needle):
                break
        if j == len(needle):
            return i-j
        return -1
        
def get_next(needle):
    nexts = [-1,]
    k = -1
    for i in range(1,len(needle)):
        if k==-1 or needle[i-1] == needle[k]:
            k+=1
            nexts.append(k)
        else:
            k = nexts[k]
            while(k>=0):
                if needle[k]!=needle[i-1]:
                    k=nexts[k]
                else:
                    break
            k+=1
            nexts.append(k)
    return nexts