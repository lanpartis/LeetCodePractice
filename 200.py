class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def paint(mark,grid,i,j):
            mark[i][j]=1
            if i-1>=0 and grid[i-1][j]=='1' and mark[i-1][j]==0:
                paint(mark,grid,i-1,j)
            if j-1>=0 and grid[i][j-1]=='1'and mark[i][j-1]==0:
                paint(mark,grid,i,j-1)
            if i+1<len(grid) and grid[i+1][j]=='1'and mark[i+1][j]==0:
                paint(mark,grid,i+1,j)
            if j+1<len(grid[0]) and grid[i][j+1]=='1'and mark[i][j+1]==0:
                paint(mark,grid,i,j+1)
        count=0
        mark = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and mark[i][j]==0:
                    count+=1
                    paint(mark,grid,i,j)
        return count
