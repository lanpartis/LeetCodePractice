class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if len(str)==0:
            return 0
        i = 0
        sign =1
        r=0
        if str[0] in {'+','-'}:
            sign = -1 if str[0] == '-' else 1
            i = 1
        while i <len(str) and ord('0')<= ord(str[i]) <= ord('9'):
            r = r*10 +int(str[i])
            i+=1
        if r >=2**31:
            r = 2**31
            if sign ==1:
                r -= 1
        return r*sign
