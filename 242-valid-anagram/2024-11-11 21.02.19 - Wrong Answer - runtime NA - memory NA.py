class Solution(object):
    def isAnagram(self, s, t):
        for i in range(len(s)):
            if s[i] not in t or t[i] not in s :
                return False
                break
        return True
        