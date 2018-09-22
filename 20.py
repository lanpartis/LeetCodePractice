class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        pair = {'(':')','[':']','{':'}'}
        left = ['(','[','{']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack)>0 and pair[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False
