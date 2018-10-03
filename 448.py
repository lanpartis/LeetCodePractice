class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=list()
        for n in nums:
            p = n if n>0 else -n
            nums[p-1]=nums[p-1] if nums[p-1]<0 else -1*nums[p-1]
        for i,n in enumerate(nums):
            if n>0:
                ans.append(i+1)
        return ans
            