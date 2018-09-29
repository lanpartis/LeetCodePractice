class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        i = 0
        j = 0
        while j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                t=nums[i+1]
                nums[i+1]=nums[j]
                nums[j]=t
                i+=1
                j+=1
        return i+1
        
        