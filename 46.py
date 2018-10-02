class Solution:
    def permute(self, nums):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result=list()
        self.step(list(),nums)
        return self.result
    def step(self,state,bag):
        if len(bag)==0:
            self.result.append(state)
            return
        for i in range(len(bag)):
            nbag=bag[:]
            del nbag[i]
            nstate=state[:]
            nstate.append(bag[i])
            self.step(nstate,nbag)
            
        