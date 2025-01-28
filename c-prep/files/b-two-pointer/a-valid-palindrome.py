"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        new_str_list = []
        for c in s:
            if c.isalnum():
                new_str_list.append(c.lower())

        p1 = 0
        n = len(new_str_list)
        while p1 < (n + 1)//2:
            if new_str_list[p1] != new_str_list[n - p1 - 1]:
                return False
            p1 += 1
        return True


# OR use 2 pointers without extra space (less comp eff, more mem eff)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left, right = 0, len(s) - 1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            
            while right > left and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left , right = left + 1, right - 1
        return True