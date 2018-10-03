#99.67%
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x>0 or y>0:
            xt = x%2
            yt = y%2
            x //= 2
            y //= 2
            ans +=xt^yt
        return ans