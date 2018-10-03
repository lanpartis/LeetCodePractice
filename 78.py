class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        for i in range(2**len(nums)):
            ans =list()
            res.append(ans)
            for j in range(len(nums)):
                if i//(2**j)%2 ==1:
                    ans.append(nums[j])
        return res

