class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        res='0'
        pos=1
        for d in num1[::-1]:
            res_i = self.m_one_digit(num2,d)
            for i in range(pos-1):
                res_i+='0'
            res = self.add(res_i,res)
            pos+=1
        zero=0
        
        return res[zero:]

        
    def m_one_digit(self,num,digit):
        digit=int(digit)
        res = ''
        c=0
        for d in num[::-1]:
            pro = int(d)*digit+c
            res = str(pro%10)+res
            c = pro//10
        if c!=0:
            res = str(c)+res
        return res
    
    def add(self,num1,num2):
        if len(num1)>len(num2):
            num1,num2=num2,num1
        c=0
        res=''
        num1=num1[::-1]
        num2=num2[::-1]
        for i in range(len(num1)):
            s=int(num1[i])+int(num2[i])+c
            res = str(s%10)+res
            c=s//10
        if len(num2)>len(num1):
            for i in range(len(num1),len(num2)):
                s = int(num2[i])+c
                res = str(s%10)+res
                c=s//10
        if c!=0:
            res = str(c) + res
        return res

