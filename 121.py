class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        mini=prices[0]
        maxi=prices[0]
        res=0
        for p in prices[1:]:
            if p>maxi:
                maxi=p
            if p<mini:
                mini=p
                maxi=p
            if maxi-mini>res:
                res = maxi-mini
        return res