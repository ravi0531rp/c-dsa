"""
242. Valid Anagram

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_ctr = Counter(s)
        t_ctr = Counter(t)
        for k, v in s_ctr.items():
            if s_ctr[k] != t_ctr[k]:
                return False
        return True
