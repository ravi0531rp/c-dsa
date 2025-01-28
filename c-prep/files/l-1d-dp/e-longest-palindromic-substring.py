"""
5. Longest Palindromic Substring
Given a string s, return the longest 
palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for idx in range(len(s)):
            l , r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result = s[l:r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1
            
            l , r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > result_len:
                    result = s[l:r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1
        return result