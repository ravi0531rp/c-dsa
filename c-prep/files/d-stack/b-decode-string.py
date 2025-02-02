class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = 0

        while idx < len(s):
            if s[idx] != ']':
                stack.append(s[idx])
            
            else:
                substring = ""
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)

                stack.append(k*substring)
            idx += 1
        return "".join(stack)


            
