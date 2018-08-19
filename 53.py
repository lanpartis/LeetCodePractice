class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        prev = nums[0]
        maxi = prev
        for i in range(1,len(nums)):
            now = self.get_max_array(prev,nums[i])
            if now>maxi:
                maxi = now
            prev = now
        return maxi

    def get_max_array(self,prev,n_ele):
        if prev<=0:
            now = n_ele
        else:
            now = prev+n_ele
        return now
