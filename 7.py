class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >=0 else -1
        x = x * sign
        r = 0
        while x>0:
            r = r*10 + x%10
            x = x//10
        if r > 2**31:
            return  0
        return sign * r
