class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for c in s:
            if c == '(':
                stack.extend([c,0])
            else:
                if len(stack)>1 and stack[-2]=='(':
                    l = stack.pop()
                    stack.pop()
                    stack[-1]+=(l+2)
                else:
                    stack.extend([c,0])
        m = 0
        for i in range(0,len(stack),2):
            if stack[i]>m:
                m=stack[i]
        return m
