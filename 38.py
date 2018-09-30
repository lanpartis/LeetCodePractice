class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            count = 1
            n_res = ''
            for i in range(len(res)):
                if i == len(res)-1:
                    n_res= n_res+str(count)+res[i]
                else:
                    if res[i]==res[i+1]:
                        count+=1
                    else:
                        n_res=n_res+str(count)+res[i]
                        count = 1
            res = n_res

        return res