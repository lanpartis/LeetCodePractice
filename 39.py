class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(candidates,target,list(),res)
        return res
        
    def dfs(self, candidates,target,path,res):
        if 0 ==target:
            res.append(path)
        else:
            for i in range(len(candidates)):
                if candidates[i] <= target:
                    n_path = path[:]
                    n_path.append(candidates[i])
                    self.dfs(candidates[i:],target-candidates[i],n_path,res)
