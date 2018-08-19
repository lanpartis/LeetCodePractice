class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        start = 0
        end = 1
        longest = 1
        hashtable = {s[start]:start}
        while end < len(s):
            if hashtable.get(s[end],-1) == -1:
                hashtable[s[end]]=end
            else:
                if end-start>longest:
                    longest = end-start
                n_start = hashtable[s[end]]+1
                for i in range(start,n_start):
                    hashtable.pop(s[i])
                hashtable[s[end]]=end
                start = n_start
            end+=1
        if end-start>longest:
            longest = end-start
        return longest
