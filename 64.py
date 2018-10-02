class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        if m==0:
            return 0
        path = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    path[i][j]=0
                elif i==0:
                    path[i][j] = path[i][j-1]
                elif j==0:
                    path[i][j] = path[i-1][j]
                else:
                    path[i][j] = min(path[i-1][j],path[i][j-1])
                path[i][j]+=grid[i][j]
        return path[-1][-1]
           