class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        symbles = ['+','-','*','/']
        stack = list()
        for t in tokens:
            if t in symbles:
                if len(stack)<2:
                    return None
                b = stack.pop()
                a = stack.pop()
                if t =='+':
                    res = a+b
                elif t=='-':
                    res = a-b
                elif t=='*':
                    res = a*b
                elif t=='/':
                    if b == 0:
                        return None
                    res = int(a/b)
                stack.append(res)
            else:
                stack.append(int(t))
        if len(stack)!= 1:
            return None
        return stack[0]
