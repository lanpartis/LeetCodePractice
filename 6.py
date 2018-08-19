class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ['' for i in range(numRows)]
        row=next_row(numRows)
        for c in s:
            res[next(row)]+=c
        res_concat=''
        for r in res:
            res_concat+=r
        return res_concat

def next_row(numRows):
    while True:
        for i in range(numRows):
            yield i
        for i in range(numRows-2,0,-1):
            yield i
