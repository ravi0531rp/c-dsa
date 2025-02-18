class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, w = len(board), len(board[0]), len(word)
        if m == 1 and n == 1:
            return word == board[0][0]

        def backtrack(position, idx):
            if idx == w:
                return True
            i,j = position
            if board[i][j] != word[idx]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"

            for r,c in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r,c), idx + 1):
                        return True
            board[i][j] = tmp
        
        for i in range(m):
            for j in range(n):
                if backtrack((i,j), 0):
                    return True
        return False
        
