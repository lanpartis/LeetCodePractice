class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x,y=0,0
        note=[[-1]*n for i in range(m)]
        return self.dfs(x,y,m,n,note)
    def dfs(self, x,y,m,n,note):
        if note[x][y]!=-1:
            return note[x][y]
        if x==m-1 and y==n-1:
            note[x][y]=1
            return 1
        res = 0
        if x<m-1:
            res += self.dfs(x+1,y,m,n,note)
        if y<n-1:
            res += self.dfs(x,y+1,m,n,note)
        note[x][y]=res
        return res