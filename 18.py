python直接用3sum的方法改到O(n^3)会超时。

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        res=list()
        nums.sort()
        two_hash={}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                l = two_hash.get(nums[i]+nums[j],list())
                l.append((i,j))
                two_hash[nums[i]+nums[j]]=l
        for i in range(len(nums)-1):
            if i>0 and nums[i-1]==nums[i]:continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]:continue
                two_sum = nums[i]+nums[j]
                oth = two_hash.get(target-two_sum,None)
                if oth:
                    for pair in oth:
                        if i not in pair and j not in pair:
                            r = [i,j,pair[0],pair[1]]
                            r.sort()
                            r=list(map(lambda x:nums[x],r))
                            if r not in res:
                                res.append(r)
        return res
