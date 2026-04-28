class Solution(object):
    def shortestPalindrome(self, s):
        if s=="":
            return ""
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[0:i] + s