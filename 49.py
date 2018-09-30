class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for s in strs:
            counter = [0] *26
            for c in s:
                counter[ord(c)-ord('a')]+=1
            
            if str(counter) in dic.keys():
                dic[str(counter)].append(s)
            else:
                dic[str(counter)]=[s,]
        res=list()
        for key in dic.keys():
            res.append(dic[key])
        return res