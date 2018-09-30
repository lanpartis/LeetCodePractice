class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        Cell = [set() for i in range(9)]                   
        Col =  [set() for i in range(9)]
        Row =  [set() for i in range(9)]

        for i,row in enumerate(board):              
            for j,num in enumerate(row):
                if num != '.':
                    k = (i//3)*3 + j//3
                    if num in Row[i] | Col[j] | Cell[k]: 
                        return False
                    Row[i].add(num)
                    Col[j].add(num)
                    Cell[k].add(num)

        return True