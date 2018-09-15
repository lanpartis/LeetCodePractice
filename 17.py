class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        cand={'2':'abc','3':'def','4':'ghi','5':'jkl',
              '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=list()
        def dfs(ans,digits,p_word):
            if len(digits)==0:
                if len(p_word)>0:
                    ans.append(p_word)
                return
            for c in cand[digits[0]]:
                word = p_word[:]
                word+=c
                dfs(ans,digits[1:],word)
        dfs(ans,digits,'')
        return ans
