class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        bucket=[False for i in range(len(nums)+1)]
        for num in nums:
            if 0<num<=len(nums):
                bucket[num-1]=True
        
        for i in range(len(bucket)):
            if not bucket[i]:
                break
        return i+1