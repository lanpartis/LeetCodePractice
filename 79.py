class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,board,word):
                    return True
        return False
    
    def dfs(self,x,y,board,word):
        if len(word)==0:
            return True
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y] != word[0]:
            return False
        else:
            board[x][y] = None
            res = self.dfs(x-1,y,board,word[1:]) or self.dfs(x+1,y,board,word[1:]) or self.dfs(x,y-1,board,word[1:]) or self.dfs(x,y+1,board,word[1:])
            board[x][y] = word[0]
            return res

            
        