class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p_zero=0
        p_one=0
        p_two=len(nums)-1
        while True:
            while p_one<len(nums)-1 and nums[p_one]!=2:
                p_one+=1
            while p_two>=0 and nums[p_two]==2:
                p_two-=1
            if p_two>p_one:
                nums[p_two],nums[p_one]=nums[p_one],nums[p_two]
            else:
                break
        if nums[p_one]==2:
            p_one-=1
        while True:
            while p_one>=0 and nums[p_one]==1:
                p_one-=1
            while p_zero<len(nums)-1 and nums[p_zero]==0:
                p_zero+=1
            if p_zero<p_one:
                nums[p_zero],nums[p_one]=nums[p_one],nums[p_zero]
            else:
                break