class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = [] 
        sol = []
        words = set(wordDict)
        n = len(s)

        def dfs(i):
            if i == n:
                res.append(" ".join(sol))
                return
            
            for j in range(i, n):
                curr_word = s[i:j+1]
                if curr_word in words:
                    sol.append(curr_word)
                    dfs(j+1)
                    sol.pop()

        dfs(0)
        return res
