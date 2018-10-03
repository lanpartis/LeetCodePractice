class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = dict()
        l=len(nums)//2
        for n in nums:
            table[n] = table.get(n,0)+1
            if table[n]>l:
                return n