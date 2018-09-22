#动态规划+hash表
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        act = dict()
        m=0
        for i in nums:
            if i in act:
                continue
            left = act.get(i-1,False)
            right = act.get(i+1,False)
            if not left and not right:
                act[i]=1
            elif left and right:
                act[i]=left + right +1
                act[i-left]=act[i]
                act[i+right]=act[i]
            elif left:
                act[i]=left+1
                act[i-left]=act[i]
            else:
                act[i]=right+1
                act[i+right]=act[i]
            if act[i]>m:
                m = act[i]
        return m
