#100%
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxP=[nums[0]]
        maxN=[nums[0]]
        for n in nums[1:]:
            if n>=0:
                if maxP[-1]>0:
                    maxP.append(maxP[-1]*n)
                else:
                    maxP.append(n)
                if maxN[-1]<0:
                    maxN.append(maxN[-1]*n)
                else:
                    maxN.append(n)
            if n<0:
                if maxP[-1]>0:
                    maxN.append(maxP[-1]*n)
                else:
                    maxN.append(n)
                if maxN[-2]<0:
                    maxP.append(maxN[-2]*n)
                else:
                    maxP.append(n)
        return max(maxP)
