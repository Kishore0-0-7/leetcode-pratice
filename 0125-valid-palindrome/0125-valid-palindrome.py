class Solution(object):
    def isPalindrome(self, s):
        ch= [cha.lower() for cha in s if cha.isalnum()]
        return ch==ch[::-1]