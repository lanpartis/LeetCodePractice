class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def d2R(one,five,ten,num):
            res=''
            if num<4:
                for i in range(num):
                    res+=one
                return res
            if num==4:
                return one+five
            if num==9:
                return one+ten
            ans=five
            for i in range(num-5):
                ans+=one
            return ans
        thou = num//1000
        hund = num%1000 //100
        tens = num%100 //10
        ones = num%10
        ans=''
        for i in range(thou):
            ans+='M'
        ans +=d2R('C','D','M',hund)
        ans +=d2R('X','L','C',tens)
        ans +=d2R('I','V','X',ones)
        return ans
