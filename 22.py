class Solution:
    result=list()
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result=list()
        self.count_lr('',0,0,n)
        return self.result
    def count_lr(self,state,left,right,n):
        state=state[:]
        if left == n :
            for i in range(left-right):
                state+=')'
            self.result.append(state)
            return
        self.count_lr(state+'(',left+1,right,n)
        if left>right:
            self.count_lr(state+')',left,right+1,n)
