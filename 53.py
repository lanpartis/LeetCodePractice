class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0] 
        running_sum=0
        for i in nums:
            running_sum+=i
            if running_sum>res:
                res = running_sum
            if running_sum<0:
                running_sum=0
        return res