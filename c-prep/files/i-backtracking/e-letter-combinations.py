class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }
        n = len(digits)
        res = [] 
        sol = []

        if not n:
            return []

        def backtrack(i):
            if i == n:
                res.append("".join(sol[:]))
                return
            
            curr = hashmap[digits[i]]
            for d in curr:
                sol.append(d)
                backtrack(i+1)
                sol.pop()
        backtrack(0)
        return res
