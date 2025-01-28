"""
647. Palindromic Substrings
Solved
Medium
Topics
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for idx in range(len(s)):
            l , r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l , r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count