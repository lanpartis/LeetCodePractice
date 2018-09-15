class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=list()
        mini=None
        tar = None
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                if mini==None or abs(s-target)<mini:
                    mini=abs(s-target)
                    tar = s
                if s >target:
                    k-=1
                elif s<target:
                    j+=1
                else:
                    return s
        return tar
