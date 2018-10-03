class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=list()
        for n in nums:
            if len(dp)==0:
                dp.append(n)
            elif len(dp)==1:
                dp.append(max(n,dp[-1]))
            else:
                dp.append(max(n+dp[-2],dp[-1]))
        return dp[-1]