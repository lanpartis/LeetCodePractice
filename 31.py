class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        mark=None
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                mark = i-1
                while i<len(nums) and nums[i]>nums[mark]:
                    i+=1
                nums[mark],nums[i-1]=nums[i-1],nums[mark]
                f=mark+1
                t=len(nums)-1
                while f<t:
                    nums[f],nums[t]=nums[t],nums[f]
                    f+=1
                    t-=1
                break
        if mark==None:
            nums.reverse()