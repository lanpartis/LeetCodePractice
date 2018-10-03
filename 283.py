#94.96%
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0=0
        p1=0
        while p1<len(nums):
            while p0<len(nums) and nums[p0]!=0:
                p0+=1
            p1=p0 if p1<p0 else p1
            while p1<len(nums) and nums[p1]==0:
                p1+=1
            if p0<len(nums) and p1<len(nums):
                nums[p0],nums[p1]=nums[p1],nums[p0]