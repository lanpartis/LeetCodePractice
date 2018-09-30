class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = nums[0]
        pos = 0
        if len(nums)==1:
            return True
        while step>0:
            pos+=1
            step = max(step-1,nums[pos])
            if pos == len(nums)-1:
                return True
        return False