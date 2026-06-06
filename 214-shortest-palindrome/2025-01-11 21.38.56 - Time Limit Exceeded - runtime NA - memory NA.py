class Solution(object):
    def shortestPalindrome(self, s):
        li = 0
        s1 = ''
        s2 = ''
        for i, c in enumerate(s):
            s1 = s1 + c
            s2 = c + s2
            
            if s1 == s2:
                li = i
        
        return ''.join(reversed(s[li+1:])) + s 