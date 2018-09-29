class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        i = 0
        j = len(nums)-1
        while i<j:
            while i<j and nums[i]!=val:
                i+=1
            while i<j and nums[j]==val:
                j-=1
            if i<j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t

        if nums[j]!=val:
            return j+1
        return i