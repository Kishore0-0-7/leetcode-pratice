class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in t or t[i] not in s :
                return False
                break
        return True
        