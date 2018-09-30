class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates,target,list(),res)
        return res
        
    def dfs(self, candidates,target,path,res):
        if 0 ==target:
            res.append(path)
        else:
            i=0
            while i < len(candidates):
                if candidates[i] <= target:
                    n_path = path[:]
                    n_path.append(candidates[i])
                    self.dfs(candidates[i+1:],target-candidates[i],n_path,res)
                i+=1
                while i<len(candidates) and candidates[i]==candidates[i-1]:
                    i+=1

