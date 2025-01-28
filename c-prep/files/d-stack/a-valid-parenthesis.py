"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 3:

Input: s = "(]"

Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        mapping = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for item in s:
            if item in mapping.keys():  
                stack.append(item)
            else:  
                if not stack or mapping[stack.pop()] != item:
                    return False
        
        return not stack  
